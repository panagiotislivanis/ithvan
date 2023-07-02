from PIL import Image
from whether import create_whether


def make_map():
    create_whether()
    # Φορτώνουμε την πρώτη εικόνα
    image1 = Image.open("images/Screenshot_2.png")

    # Φορτώνουμε τη δεύτερη εικόνα
    image2 = Image.open("images/whether.png")

    image1.paste(image2, (1570, 0))
    # image1.resize((1000,700))
    print("Saving image as PNG...")
    image1.save("images/final_2.png")
    print("Image saved as whether.PNG")


# schedule.every(1).second.do(repeat)
# while True:

#   schedule.run_pending()
#   time.sleep(1)
