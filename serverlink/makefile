BOOST = /home/jack/docs/boost/
CLIENT_FILE = quadmotion_client
SERVER_FILE = quadmotion_server

all: clean quadmotion_client quadmotion_server

quadmotion_client:
	g++ -o quadmotion_client \
	./client/main.cpp \
	-I $(BOOST) \
	-L $(BOOST)/libs \
	-l boost_system \
	-l pthread

quadmotion_server:
	g++ -o quadmotion_server \
	./server/main.cpp \
	-I $(BOOST) \
	-L $(BOOST)/libs \
	-l boost_system \
	-l pthread

clean:
ifneq ("$(wildcard $(CLIENT_FILE))","")
	rm $(CLIENT_FILE)
endif
ifneq ("$(wildcard $(SERVER_FILE))","")
	rm $(SERVER_FILE)
endif
