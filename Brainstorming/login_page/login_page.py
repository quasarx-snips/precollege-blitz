import time
import pickle

name = input("Enter Name").lower()
pw = input("Password").lower()
#directory = {}
#with open("user_db.dat", "wb") as file:
#    pickle.dump(directory, file)

"""with open("user_db.dat", "wb") as file:
    pickle.dump(directory, file)
    file.close()
"""
with open ("user_db.dat", "rb") as file:
    directory = pickle.load(file)
    if name in directory:
      if pw == directory[name][0]:
        print("Access Granted")
      else:
        print("Access Denied")
    else:
        with open("user_db.dat", "wb") as file:
            if len(directory) > 0:
                last_user_key = next(reversed(directory))
                last_user_time = directory[last_user_key][1]

                if (time.time() - last_user_time) < 10:
                    print("Rate Limit")
                    pickle.dump(directory, file)
                else:
                    directory[name] = [pw, time.time()]
                    pickle.dump(directory, file)
                    print("User Created")
            else:

                directory[name] = [pw, time.time()]
                pickle.dump(directory, file)
                print("User Created")
