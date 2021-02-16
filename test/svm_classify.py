from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score


class SulfoSVM: 
    def __init__(self, x, y, test_size): 
        self.x = x
        self.y = y.ravel()
        self.test_size = test_size
        self.model = None 

        if self.model is None: 
            self.model = self.get_model()
        
    def split(self): 
        self.x_train, self.x_test, self.y_train, self.y_tesst = train_test_split(self.x, self.y, 
                                                test_size=self.test_size, random_state=42)

    def get_model(self): 
        return SVC(C=2, kernel="linear")


    def train(self): 
        return self.model.fit(self.x, self.y)


    def test(self): 
        return self.model.predict(self.x)


    def cros_validate(self): 
        return cross_val_score(self.train(), self.x, self.y, cv=2)