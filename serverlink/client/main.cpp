// CLIENT MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>

using boost::asio::ip::tcp;
using namespace std;

const int PACKET_SIZE = 64; // the max packet length is 64 characters (we only use 1)

int main() {
    cout << "-- CLIENT SERVICE --" << endl;
    boost::asio::io_service ioservice; // ioservice

    tcp::resolver resolver(ioservice); // used to find the ip address
    tcp::resolver::query query("127.0.0.1", "1234"); // our query...
    tcp::socket socket(ioservice); // the socket
    while (true) { // infinite loops ensures it keeps going even in error
        try {
            char signal; // the signal character 
            
            char output[PACKET_SIZE] = { signal }; // set the output to the signal

            boost::asio::connect(socket, resolver.resolve(query)); // connect to server
            boost::asio::write(socket, boost::asio::buffer(output, PACKET_SIZE)); // send packet
        }

        catch (exception& e) {
            cout << "EXCEPTION: " << e.what() << endl;
        }   
    }

    return 1;
}

// GET THE SIGNAL HERE
char get_signal() {
    char signal;
    cout << "enter signal: "; cin >> signal;
    return signal;
}