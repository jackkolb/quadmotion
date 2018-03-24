// SERVER MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/optional.hpp>
#include <vector>
#include <string>

using namespace std;
using boost::asio::ip::tcp;

class Connection {
    public:
        void process_command(tcp::socket&, string);
        int MAX_PACKET_LENGTH = 64;
};

int main() {
    // initialize service
    boost::asio::io_service ioservice;

    while (true) {
        try {
            Connection session;
            int port = 1234;
            tcp::acceptor acceptor (ioservice, tcp::endpoint(tcp::v4(), port));
            tcp::socket _socket(ioservice);

            acceptor.accept(_socket);

            char input_buffer[64];
            boost::asio::read(_socket, boost::asio::buffer(input_buffer, 64));
            session.process_command(_socket, input_buffer);
        }
        catch (exception& e) {
            cerr << "EXCEPTION: " << e.what() << endl;
        }
    }
    return 1;
}

void Connection::process_command(tcp::socket& socket, string a) {
    cout << "DATA: " << a << endl;
    return;
}