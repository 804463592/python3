#import TemperatureConversion
#from TemperatureConversion import c2f,f2c
import package1.TemperatureConversion as tc#最推荐的方式

#print("32摄氏度=%.2f华氏度"%TemperatureConversion.c2f(32))
#print("99华氏度=%.2f摄氏度"%TemperatureConversion.f2c(99))

#print("32摄氏度=%.2f华氏度"%c2f(32))
#print("99华氏度=%.2f摄氏度"%f2c(99))

print("32摄氏度=%.2f华氏度"%tc.c2f(32))
print("99华氏度=%.2f摄氏度"%tc.f2c(99))
