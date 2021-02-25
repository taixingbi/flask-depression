import time, json, requests

class test_call_api:
    def __init__(self, filename):
        print("\n-------------------test_call_api-------------------" )
        self.filename= filename

    def api_post(self, data):
        URL= 'http://127.0.0.1:8071/api/depression'

        jsonData = json.dumps(data)
        print(jsonData)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(  URL,
                            data= jsonData,
                            headers= headers)

        return r

    def call_api_depression(self):
        data_req= {
            "filename": self.filename,
        }

        time_try_again= 1
        while time_try_again >= 0:
            r= self.api_post(data_req)
            print(r.status_code)
            if r.status_code == 200:
                return r.json()

            time_try_again= time_try_again -1

        return []

if __name__=="__main__":
    filename= '/Volumes/disk2/ml-kaden-data-interface-test/flask_depression/data/163_1613840232_1m_noSilence.wav'

    depressions= test_call_api(filename).call_api_depression()
    print(depressions)
