import hashlib
import json
from hashlib import md5


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def main():
    result = []
    with open("example_data.json", "r") as f:
        data = json.load(f)

    for item in data:
        result.append(computeMD5hash(str(item))+":" +str(item))


    with open(r'result.frigo', 'w') as fp:
        for item in result:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')
    print(result)
    pass



if __name__ == "__main__":
    main()