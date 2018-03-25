// SERVER MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/optional.hpp>
#include <string>

using namespace std;
using boost::asio::ip::tcp;

const int PACKET_SIZE = 64; // packets will be 64 characters (although only 1 will be used)!

int main() {
    cout << "-- SERVER SERVICE --" << endl;
    while (true) { // makes the server go infinitely
        try {
            boost::asio::io_service ioservice; // initialize service
            int port = 1234; // port we are looking on
            tcp::acceptor acceptor (ioservice, tcp::endpoint(tcp::v4(), port)); // create acceptor mechanism
            tcp::socket socket(ioservice); // create socket

            acceptor.accept(socket); // wait for a connection, redirect it to the socket

            char input_buffer[PACKET_SIZE]; // this is the receiving buffer
            boost::asio::read(socket, boost::asio::buffer(input_buffer, 64)); // read data from the socket (blocks until buffer fills)
            cout << "data received: ";
            process_command(socket, input_buffer); // process the input
            cout << endl;
        }
        catch (exception& e) {
            cerr << "EXCEPTION: " << e.what() << endl;
        }
    }
    return 1;
}

// PUT SERIAL IO STUFFS HERE!!
void process_command(tcp::socket& socket, string a) {
    cout << a;
    return;
}