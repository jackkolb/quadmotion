// CLIENT MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>

using boost::asio::ip::tcp;
using namespace std;

const int PACKET_SIZE = 64;

int main() {
    cout << "-- CLIENT SERVICE --" << endl;
    boost::asio::io_service ioservice;
    tcp::resolver resolver(ioservice);
    tcp::resolver::query query("127.0.0.1", "1234");
    tcp::socket socket(ioservice);
    while (true) {
        try {
            char signal;
            cout << "enter signal: "; cin >> signal;
            char output[PACKET_SIZE] = { signal };

            boost::asio::connect(socket, resolver.resolve(query)); // connect to server
            boost::asio::write(socket, boost::asio::buffer(output, PACKET_SIZE)); // send packet
        }

        catch (exception& e) {
            cout << "EXCEPTION: " << e.what() << endl;
        }   
    }

    return 1;
}