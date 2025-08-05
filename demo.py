import logging

logging.basicConfig(level=logging.INFO, force=True)

from rag.app import naive, paper


FACTORY = {
    "general": naive,
    "naive": naive,
    "paper": paper,
}


if __name__ == "__main__":
    file_path = "/mnt/c/Users/zzy/Desktop/rag_test.docx"
    # file_path = "/mnt/c/Users/zzy/Desktop/pic_one.pdf"

    def dummy(msg="", msg2=""):
        print(str(msg) + " --- " + str(msg2))

    file_type = "naive"
    chunker = FACTORY[file_type]

    res = chunker.chunk(file_path, callback=dummy)
    print(res)
