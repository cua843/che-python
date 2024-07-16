import machine 
import time
#import onewire
#import ds18x20

TdsSensorPin = 0  # 類比引腳
#TemperatureSensorPin = 22  # 溫度感測器引腳
VREF = 5.0# 類比轉換器的參考電壓(V)
SCOUNT = 30  # 樣本點數

delay_time = 1  # 每讀一筆資料的間隔時間（秒）
print_interval = 0.8  # 輸出間隔時間（秒）

analogBuffer = [0] * SCOUNT
analogBufferIndex = 0
tds_no = 1

adc_tds = machine.ADC(TdsSensorPin)
#adc_temp = ds18x20.DS18X20(onewire.OneWire(Pin(TemperatureSensorPin)))

while True:  

    # 讀取模擬數據並存儲到緩衝區中    
    analogBuffer[analogBufferIndex] = adc_tds.read_u16()     
    analogBufferIndex = (analogBufferIndex + 1) % SCOUNT
    
    if analogBufferIndex == 0:
        averageVoltage = sum(analogBuffer) / SCOUNT * VREF / 117540
        temperature = 25
        compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0)
        compensationVolatge = averageVoltage / compensationCoefficient            
        tdsValue = (133.42 * compensationVolatge * compensationVolatge * compensationVolatge - 255.86 * compensationVolatge * compensationVolatge + 857.39 * compensationVolatge) * 0.5 #convert voltage value to tds value
            
        print("電壓:,{:.2f},V,TDS:,{:.0f},ppm".format(averageVoltage,tdsValue))
        

    
    time.sleep_ms(100)  # 每隔800毫秒輸出一次
