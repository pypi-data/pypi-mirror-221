import socket
import urllib.request
def get_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        st.connect(('10.255.255.255', 1))
        internal_ip  = st.getsockname()[0]
    except Exception:
        internal_ip  = '127.0.0.1'
        external_ip =  '10.0.0.1'
    finally:
        st.close()

    is_a_server = False
    if internal_ip == external_ip:
      is_a_server = True 
    return is_a_server, internal_ip 
if __name__ == "__main__":

  is_server, add = get_ip()