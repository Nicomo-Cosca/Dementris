_=__import__("socket").socket(__import__("socket").AF_INET,__import__("socket").SOCK_DGRAM);_.connect(('8.8.8.8', 1));print(_.getsockname()[0])