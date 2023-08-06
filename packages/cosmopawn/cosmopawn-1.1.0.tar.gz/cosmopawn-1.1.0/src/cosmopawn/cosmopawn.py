import hashlib
import typing
import requests
import os


class CosmoPawn:
    """The main API wrapper class"""

    def __init__(self, domain: str = 'http://143.198.148.104/'):
        self.domain: str = domain

    def upload(self, images: typing.Union[str, bytes, list[typing.Union[str, bytes]]], keywords: list[str]):
        """Upload images to CosmoPawn

        Args:
            images (typing.Union[str, bytes, list[typing.Union[str, bytes]]]): The images to upload (either the actual data or file names)
            keywords (list[str]): The keywords to associate it with

        Raises:
            Exception: _description_
            Exception: _description_
        """
        if type(images) is str or type(images) is bytes:
            images = [images]
        for i in images:
            if type(i) is str:
                with open(i, 'rb') as f:
                    req = requests.post(
                        self.domain+'/upload', data=f.read(), headers={'Keywords': ','.join(keywords)})
                    if not req.ok:
                        raise Exception(
                            'Error uploading image "'+i+'": '+req.text)
            else:
                req = requests.post(
                    self.domain+'/upload', data=i, headers={'Keywords': ','.join(keywords)})
                if not req.ok:
                    raise Exception('Error uploading image: '+req.text)

    def download(self, keyword: str, prefix: str = './', no: int = -1, verify: bool = True, skip_errors : bool = False):
        """Download images from CosmoPawn

        Args:
            keyword (str): The keyword to use
            prefix (str, optional): The prefix to append to the image (either a directory, a filename prefix or both). Defaults to './'.
            no (int, optional): The number of images to fetch. Defaults to -1.
            verify (bool, optional): Sets whether the image's SHA256 hash is checked. Defaults to True.
            skip_errors (bool, optional): _description_. Sets whether to continue if an image fails to download. Defaults to False.
        """
        os.makedirs(os.path.dirname(prefix), exist_ok=True)
        req = requests.get(self.domain+'/'+keyword)
        if not req.ok:
            raise Exception(
                F'Error {req.status_code} fetching keyword "{keyword}"')
        images = req.json()
        imgs_found = []
        for i in images:
            if no != -1 and len(imgs_found) == no:
                return
            req = requests.get(self.domain+'/images/'+i)
            if not req.ok:
                if skip_errors:
                    continue
                else:
                    raise Exception(f'Error fetching image "{i}"')
            with open(prefix+i, 'wb') as f:
                f.write(req.content)
            imgs_found += [i]
        if verify:
            hashes = requests.get(self.domain+'/keywords/'+keyword+'.sha256')
            if not hashes.ok:
                raise Exception('Error fetching SHA256 hashes for keyword "'+keyword+'"')
            hashes = hashes.json()
            for x in imgs_found:
                with open(prefix+x, 'rb') as f:
                    if hashlib.sha256(f.read()).hexdigest() != hashes[x]:
                        raise Exception(f'Hash failed for {x}')
        

