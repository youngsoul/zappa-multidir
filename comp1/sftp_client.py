import paramiko

password = 'demo-user'
username = 'demo-user'
host = 'demo.wftpserver.com'
port = 2222

def test_sftp():

    # Open a transport

    transport = paramiko.Transport((host, port))

    # Auth

    transport.connect(username = username, password = password)

    # Go!

    sftp = paramiko.SFTPClient.from_transport(transport)

    result = sftp.listdir()
    print(result)

    # # Download
    # filepath = '/AR'
    # localpath = './junk'
    # sftp.get(filepath, localpath)
    #
    # # Upload
    # filepath = '/home/foo.jpg'
    # localpath = '/home/pony.jpg'
    # sftp.put(localpath, filepath)


    # Close
    sftp.close()
    transport.close()
    return result

if __name__ == '__main__':
    test_sftp()