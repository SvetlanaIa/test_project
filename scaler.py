'''
Реализовать класс Scaler, выполняющий стандартизацию входного вектора (среднее = 0, дисперсия = 1):
- класс должен содержать метод .fit(), вызов которого выполняет подсчет и сохранение среднего и дисперсии 
входного вектора
- класс должен содержать метод .transform(), вызов которого использует сохраненные параметры и стандартизирует
входной вектор (в случае отсутствия сохраненных параметров должно генерироваться исключение)
- класс должен содержать метод .fit_transform(), являющийся комбинацией соответствующих методов
'''

import math 

class Scaler():
    def __init__(self):
      #  self.arr = arr
        pass 

    def fit(self,arr):
        if type(arr) != list:
            raise TypeError("type must be a list")

        for i in arr:
            if math.floor(i) != i:
                raise TypeError("type must in list must be int or float")
        
        self.arr = arr
        res = {}
        
        count = 0
        for i in arr:
            count +=i
        res['mean']=count/len(arr)

        sum = 0
        for i in arr:
            sum += (i-res['mean'])**2
            
        res['var']= sum/len(arr)
        self.res_ = res
        return self.res_
    
    def transform(self,arr2):
        if type(arr2) != list:
            raise TypeError("type must be a list")

        for i in arr2:
            if math.floor(i) != i:
                raise TypeError("type must in list must be int or float")    

        res_arr = []
        if not self.arr:
            raise TypeError("please use fit")
              
        for i in arr2:
            res_arr.append((i-self.res_['mean'])/(self.res_['var'])**0.5)
        return res_arr

    def fit_transform(self,arr):
        self.fit(arr)
        return self.transform(arr)


if __name__ == '__main__':
    a = Scaler()
    print(a.fit([1,2,3,4]))
    print(a.transform([1,2,3,4,5]))
    print(a.fit_transform([1,2,3,4,5]))
