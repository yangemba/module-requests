import socket

class Request:

    def get(adress):
        adress_string = "GET / HTTP/1.1\nHost: %s \n\n" % (adress)
        request = bytes(adress_string, encoding='utf-8')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("cnn.com", 80))
        s.send(request)
        result = s.recv(10000)

        s = str(result)
        # print(s)

        response = s.split("\\r\\n")
        return response


class Response:

    def __init__(self, response):
        counter = 0
        for element in response:
            if element == "":
                break
            else:
                counter += 1

        first = response[0].split(" ")
        second = response[1:counter]
        second_keys = []
        second_values = []

        for element in second:
           temp = element.split(':')
           second_keys.append(temp[0])
           second_values.append(temp[1])

        headers_dict = dict(zip(second_keys, second_values))

        self.protocol = first[0].replace('"', '').replace('b', '').replace('\'', '')
        self.code = first[1]
        self.status = first[2].replace('"', '')
        self.headers = headers_dict
        self.body = response[counter + 1:]


if __name__ == '__main__':

    with open('setting.txt', 'r') as file:
        file.seek(0)
        text = file.read()

    response = Request.get(text)

    print('\x1b[6;30;42m' + 'Protocol:' + '\x1b[0m')
    print(Response(response).protocol)
    print('\x1b[6;30;42m' + 'Code:' + '\x1b[0m')
    print(Response(response).code)
    print('\x1b[6;30;42m' + 'Status:' + '\x1b[0m')
    print(Response(response).status)
    print('\x1b[6;30;42m' + 'Headers:' + '\x1b[0m')
    print(Response(response).headers)
    print('\x1b[6;30;42m' + 'Body:' + '\x1b[0m')
    print(Response(response).body)

