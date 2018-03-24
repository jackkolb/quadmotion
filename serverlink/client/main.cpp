// CLIENT MAIN.CPP!!!

#include <iostream>
#include <boost/asio.hpp>
#include <boost/array.hpp>
#include <vector>

using boost::asio::ip::tcp;
using namespace std;

int PACKET_SIZE = 64;

int main() {
    try {
        boost::asio::io_service ioservice;
        tcp::resolver resolver(ioservice);
        tcp::resolver::query query("127.0.0.1", "1234");
        tcp::socket socket(ioservice);

        char output[PACKET_SIZE] = { 'r' };

        cout << "Press enter to send signal" << endl;
        string trash; cin >> trash;

        boost::asio::connect(socket, resolver.resolve(query));
        boost::asio::write(socket, boost::asio::buffer(output, PACKET_SIZE));
    }

    catch (exception& e) {
        cout << "EXCEPTION: " << e.what() << endl;
    }

    return 1;
}