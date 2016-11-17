#include <boost/asio.hpp>
#include <boost/bind.hpp>

#include <iostream>
#include <sstream>

using namespace boost::asio;
using boost::system::error_code;

io_service service;

std::string handle(const std::string& req)
{
    std::stringstream response_body;
    response_body << "<title>Test C++ HTTP Server</title>\n"
        << "<h1>Test page</h1>\n"
        << "<p>This is body of the test page...</p>\n"
        << "<h2>Request headers</h2>\n"
        << "<pre>" << req << "</pre>\n"
        << "<em><small>Test C++ Http Server</small></em>\n";

    std::stringstream response;
    response << "HTTP/1.1 200 OK\r\n"
        << "Version: HTTP/1.1\r\n"
        << "Content-Type: text/html; charset=utf-8\r\n"
        << "Content-Length: " << response_body.str().length()
        << "\r\n\r\n"
        << response_body.str();

    return response.str();
}

size_t read_complete(char * buff, const error_code & err, size_t bytes) {
    if (err) return 0;
    for (char* b = buff; b < buff + bytes - 3; ++b) {
        if (*b == '\r' && *(b + 1) == '\n'
                && *(b + 2) == '\r' && *(b + 3) == '\n') {
            return 0;
        }
    }
    return 1;
}

void handle_connections() {
    ip::tcp::acceptor acceptor(service, ip::tcp::endpoint(ip::tcp::v4(), 8001));
    char buff[1024];
    while (true) {
        ip::tcp::socket sock(service);
        acceptor.accept(sock);
        int bytes = read(sock, buffer(buff),
            boost::bind(read_complete, buff, _1, _2));
        std::string msg(buff, bytes);
        sock.write_some(buffer(handle(msg)));
        sock.close();
    }
}

int main()
{
    handle_connections();
    return 0;
}
