# v0.0.2

from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import json
import subprocess

class py4AxisStage:
    class Axis:
        x = 0
        y = 1
        z = 2
        stay = 3
    class Coord:
        ABS = 0
        REL = 1
    class _socket_setting:
        port_send = 9000  # Python→C++
        port_recv = 9001  # C++→Python
        address = "127.0.0.1"
    class StageError(Exception):
        pass

    def __init__(self):
        self._s_send = socket(AF_INET, SOCK_DGRAM)
        self._s_recv = socket(AF_INET, SOCK_DGRAM)
        self._s_recv.bind((self._socket_setting.address, self._socket_setting.port_recv))
        try:
            self._cpp_app = subprocess.Popen(r"C:\Users\hmi\Documents\nishimura\build\My4axisStage_for_ExternalControl\debug\My4axisStage_for_ExternalControl.exe")
        except FileNotFoundError:
            raise self.StageError('4軸ステージが接続されていないPCの可能性があります')
            exit()
        self._th_monitor_pos = Thread(target=self._get_position, daemon=True)
        self._th_monitor_pos.start()
        self.position = {}
        while len(self.position) == 0:
            pass
    def _get_position(self):
        msg_recv, _ = self._s_recv.recvfrom(2048)
        self.position = json.loads(msg_recv.decode().replace('\x00', ''))
    def send_command(self, axis, speed, distance, coord):  # logファイルと同じ形式でデータ送信（No.は不要）：[軸，速度，移動量]
        msg = '{ax},{co},{sp},{dist}'.format(ax=axis, sp=speed, dist=distance, co=coord)
        self._s_send.sendto(msg.encode(), (self._socket_setting.address, self._socket_setting.port_send))
    def stop(self):
        msg = 'stop'
        self._s_send.sendto(msg.encode(), (self._socket_setting.address, self._socket_setting.port_send))
    def exit(self):
        self._s_recv.close()
        self._s_send.close()
        self._cpp_app.terminate()
