class BaseView():
    def __init__(self,dr):
        self.dr=dr

    def find_element(self,loc):
        return self.dr.find_element(*loc)

    def find_elements(self,loc):
        return self.dr.find_elements(*loc)

    def get_window_size(self):
        return self.dr.get_window_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.dr.swipe(start_x,start_y,end_x,end_y,duration)

    def close(self):
        return self.dr.close_app()