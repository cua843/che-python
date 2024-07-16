import serial
import matplotlib.pyplot as plt

COM_PORT = '/dev/ttyUSB0'
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES)
no = 1
x_data = []
y_data = []

plt.ion()  # 啟用交互式模式

while True:
    while ser.in_waiting:
        data_raw = ser.readline()
        data = data_raw.decode().strip().split(",")  # 移除換行符並以逗號分割
        print(data)
        
        # 假設從串列讀取了兩個數值
        if len(data) >= 2:
            x_data.append(no)
            y_data.append(float(data[4]))  # 將第一個數值作為 y 軸的值
            no += 1
            
            # 繪製折線圖
            plt.clf()  # 清除當前圖形
            plt.plot(x_data, y_data)
            #plt.xlabel('')
            plt.ylabel('ppm')
            plt.title('TDS')
            plt.pause(0.01)  # 暫停一小段時間以便圖形更新

plt.ioff()  # 關閉交互式模式
plt.show()  # 顯示最終圖形