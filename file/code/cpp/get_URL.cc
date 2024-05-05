void get_URL( const string& host, const string& path )
{
  clog << "Your Host is: " << host << ", visit path is : " << path << "\n";
  // find the host address
  Address hostAddress = Address(host, "http");
  clog << "building socket ...\n";
  // try to build a TCP socket
  TCPSocket socket = TCPSocket();
  socket.connect(hostAddress); // connect to host address
  clog << "local_address: " << socket.local_address().to_string() <<
          "\npeer_address: " << socket.peer_address().to_string() << "\n";
  // begin to write
  string str1 = "GET " + path + " HTTP/1.1\r\n";
  string str2 = "Host: " + host + "\r\n";
  string str3 = "Connection: close\r\n";
  string end = "\r\n";
  socket.write(str1);
  socket.write(str2);
  socket.write(str3);
  socket.write(end);
  // begin to read
  string output;
  while (! socket.eof()) {
    socket.read(output);
    cout << output;
  }
  socket.close();
}