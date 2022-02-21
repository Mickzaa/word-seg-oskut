from helper import OSKut, load_model


class ExpCut():
    def __init__(self, engine='lst20'):
        self.engine = engine
        load_model(engine=self.engine)

    def predict_(self, text):
        return OSKut(text)


if __name__ == '__main__':
    exp_word_seg = ExpCut()
    text = 'วันนี้กินอะไรดี'

    result = exp_word_seg.predict_(text)
    print(result)
