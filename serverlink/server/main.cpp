// SERVER MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/optional.hpp>
#include <vector>
#include <string>

using namespace std;
using boost::asio::ip::tcp;

const int PACKET_SIZE = 64;

class Connection {
    public:
        void process_command(tcp::socket&, string);
};

int main() {
    while (true) { // makes the server go infinitely
        try {
            boost::asio::io_service ioservice; // initialize service
            Connection session; // create session 
            int port = 1234; // port we are looking on
            tcp::acceptor acceptor (ioservice, tcp::endpoint(tcp::v4(), port)); // create acceptor mechanism
            tcp::socket socket(ioservice); // create socket

            acceptor.accept(socket); // wait for a connection, redirect it to the socket

            char input_buffer[PACKET_SIZE]; // this is the receiving buffer
            boost::asio::read(socket, boost::asio::buffer(input_buffer, 64)); // read data from the socket (blocks until buffer fills)
            session.process_command(socket, input_buffer); // process the input
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