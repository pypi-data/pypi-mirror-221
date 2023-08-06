# CosmoPawn-Py : An API wrapper for [CosmoPawn](https://github.com/pennacap/cosmo-pawn) in Python
## Installation
```sh
pip install cosmopawn
# or
pip3 install cosmopawn
# or
pip install git+https://github.com/pennacap/cosmopawn-py
```
## Usage
```py
import cosmopawn
wrapper = cosmopawn.CosmoPawn() # Or pass in an IP address / domain
wrapper.download('dog', prefix='dog_pics/dog', no=10) # downloads 10 dog pictures, prefixing their file name with dog and saving it to dog_pics/
wrapper.upload(['file1.jpg', 'file2.png'], ['keyword1', 'keyword2']) # upload file1.jpg and file2.png with keywords keyword1 and keywords2
```

