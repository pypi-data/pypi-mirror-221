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
                req = requests.post(self.domain+'/upload', data=i, headers={'Keywords': ','.join(keywords)})
                if not req.ok:
                    raise Exception('Error uploading image: '+req.text)

    def download(self, keyword: str, prefix: str = '', save_to: str = '.', no: int = -1):
        os.makedirs(save_to, exist_ok=True)
        req = requests.get(self.domain+'/'+keyword)
        if not req.ok:
            raise Exception(
                F'Error {req.status_code} fetching keyword "{keyword}"')
        images = req.json()
        count = 0
        for i in images:
            if no != -1 and count == no:
                return
            req = requests.get(self.domain+'/images/'+i)
            if not req.ok:
                continue
            with open(save_to+'/'+prefix+i, 'wb') as f:
                f.write(req.content)
            count += 1
    
