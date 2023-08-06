from aityz import exceptions

def pad(pad, length=16):
    """
    Pad a given string `pad` with spaces to a specified `length`.

    :param pad: The string to be padded.
    :param length: The desired length of the padded string. Default is 16.
    :return: The padded string.
    """
    lenPad = len(pad) % length
    return pad + (length - lenPad) * ' '


class RSA:
    """
    Initialize an RSA object.

    :param bits: The number of bits for the RSA key. Default is 2048.
    :param fromFile: If set to True, the constructor expects the priKey and pubKey parameters to be provided and loads the RSA keys from the specified files. Default is False.
    :param priKey: The path to the file containing the private key in PKCS1 format. Required if fromFile is True.
    :param pubKey: The path to the file containing the public key in PKCS1 format. Required if fromFile is True.
    """

    def __init__(self, bits=2048, fromFile=False, priKey=None, pubKey=None):
        """
        :param bits: The number of bits for the RSA key. Default is 2048.
        :param fromFile: If set to True, the constructor expects the priKey and pubKey parameters to be provided and loads the RSA keys from the specified files. Default is False.
        :param priKey: The path to the file containing the private key in PKCS1 format. Required if fromFile is True.
        :param pubKey: The path to the file containing the public key in PKCS1 format. Required if fromFile is True.
        """
        super().__init__()
        if fromFile:
            print('From File is True, Using priKey and pubKey variables!')
            if priKey is None or pubKey is None:
                raise exceptions.InitialisationError
            else:
                with open(pubKey, 'rb') as f:
                    pub_key_data = f.read()
                    self.Pub = rsa.PublicKey.load_pkcs1(pub_key_data)

                with open(priKey, 'rb') as f:
                    pri_key_data = f.read()
                    self.Pri = rsa.PrivateKey.load_pkcs1(pri_key_data)
        else:
            print('Generating RSA Keys...')
            self.Pub, self.Pri = rsa.newkeys(bits)

    def save(self, priKey='priKey.pem', pubKey='pubKey.pem'):
        """
        Save the RSA private and public keys to files.

        :param priKey: The file name to save the private key. Default is 'priKey.pem'.
        :param pubKey: The file name to save the public key. Default is 'pubKey.pem'.
        :return: None
        """
        with open(priKey, 'wb') as f:
            f.write(self.Pri.save_pkcs1())

        with open(pubKey, 'wb') as f:
            f.write(self.Pub.save_pkcs1())

    def encrypt(self, content):
        """
        Encrypts the given content using the RSA encryption algorithm.

        :param content: The content to be encrypted.
        :return: The encrypted content.
        """
        return rsa.encrypt(content, self.Pub)

    def encryptFile(self, filename, outputFile=None):
        """
        Encrypts the contents of the file with RSA encryption.

        :param filename: The path to the input file.
        :param outputFile: The path to the output file. (optional)
        :return: The encrypted data if `outputFile` is not provided.
        """
        with open(filename, 'rb') as f:
            data = f.read()
            f.close()
        encData = rsa.encrypt(data, self.Pub)
        if outputFile is not None:
            with open(outputFile, 'wb') as f:
                f.write(encData)
        else:
            return encData

    def decrypt(self, content):
        return rsa.decrypt(content, self.Pri)

    def decryptFile(self, filename, outputFile=None):
        with open(filename, 'rb') as f:
            data = f.read()
            f.close()
        Data = rsa.decrypt(data, self.Pri)
        if outputFile is not None:
            with open(outputFile, 'wb') as f:
                f.write(Data)
        else:
            return Data
