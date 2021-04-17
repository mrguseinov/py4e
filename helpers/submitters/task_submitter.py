from typing import Callable, Literal

from helpers.submitters.task_submitter_base import TaskSubmitterBase

_ALL_DATA = {
    "01.1": [([], "Hello, World!\n")],
    "02.1": [(["Random"], "Enter your name:\nHello, Random!\n")],
    "02.2": [(["45", "2.625"], "Enter hours:\nEnter rate:\nGross pay: 118.12\n")],
    "02.3": [
        (["15.67"], "Enter Celsius temperature:\nFahrenheit temperature: 60.21\n")
    ],
    "03.1": [
        (["36", "1.456"], "Enter hours:\nEnter rate:\nGross pay: 52.42\n"),
        (["40", "2.1"], "Enter hours:\nEnter rate:\nGross pay: 84.0\n"),
        (["45.123", "3.456"], "Enter hours:\nEnter rate:\nGross pay: 164.8\n"),
    ],
    "03.2": [
        (
            ["45", "2.625"],
            "Enter hours:\nEnter rate:\nGross pay: 118.12\n",
        ),
        (
            ["10", "Random"],
            "Enter hours:\nEnter rate:\nError! Enter only numeric input.\n",
        ),
        (
            ["Random"],
            "Enter hours:\nError! Enter only numeric input.\n",
        ),
    ],
    "03.3": [
        (["1.01"], "Enter score:\nError! Score is out of range [0.0, 1.0].\n"),
        (["1"], "Enter score:\nGrade: A\n"),
        (["0.9"], "Enter score:\nGrade: A\n"),
        (["0.8"], "Enter score:\nGrade: B\n"),
        (["0.7"], "Enter score:\nGrade: C\n"),
        (["0.6"], "Enter score:\nGrade: D\n"),
        (["0.55"], "Enter score:\nGrade: F\n"),
        (["0"], "Enter score:\nGrade: F\n"),
        (["-0.01"], "Enter score:\nError! Score is out of range [0.0, 1.0].\n"),
        (["Random"], "Enter score:\nError! Enter only numeric input.\n"),
    ],
    "04.1": [
        ([36, 1.456], 52.42),
        ([40, 2.2], 88.0),
        ([45.123, 3.456], 164.8),
    ],
    "04.2": [
        ([1.01], ValueError("Error! Score is out of range [0.0, 1.0].")),
        ([1], "A"),
        ([0.9], "A"),
        ([0.8], "B"),
        ([0.7], "C"),
        ([0.6], "D"),
        ([0.55], "F"),
        ([0], "F"),
        ([-0.01], ValueError("Error! Score is out of range [0.0, 1.0].")),
    ],
    "05.1": [
        (
            [1, "Random", "done"],
            "Enter a number:\nEnter a number:\nError: Invalid input.\nEnter a number:\n"
            "\nTotal: 1.0\nCount: 1\nAverage: 1.0\n",
        ),
        (
            [1.222, 2, 3.555, "done"],
            "Enter a number:\nEnter a number:\nEnter a number:\nEnter a number:\n\n"
            "Total: 6.777\nCount: 3\nAverage: 2.259\n",
        ),
    ],
    "05.2": [
        (
            [1, "Random", "done"],
            "Enter a number:\nEnter a number:\nError: Invalid input.\nEnter a number:\n"
            "\nMinimum is 1\nMaximum is 1\n",
        ),
        (
            [1, -1, 3, "done"],
            "Enter a number:\nEnter a number:\nEnter a number:\nEnter a number:\n"
            "\nMinimum is -1\nMaximum is 3\n",
        ),
        (
            [10, -10, 3.1, "done"],
            "Enter a number:\nEnter a number:\nEnter a number:\nError: Invalid input.\n"
            "Enter a number:\n\nMinimum is -10\nMaximum is 10\n",
        ),
    ],
    "06.1": [
        (
            ["I like coding!"],
            "Enter one line of text:\n!\ng\nn\ni\nd\no\nc\n \ne\nk\ni\nl\n \nI\n",
        ),
        (
            ["I like sport!"],
            "Enter one line of text:\n!\nt\nr\no\np\ns\n \ne\nk\ni\nl\n \nI\n",
        ),
    ],
    "06.2": [
        (["X-DSPAM-Confidence: 0.1"], 0.1),
        (["X-DSPAM-Confidence:    0.999"], 0.999),
        (["X-DSPAM-Confidence:    0.8475"], 0.8475),
    ],
    "06.3": [
        (["I love Python!", "o"], 2),
        (["I like music and cooking!", "i"], 3),
    ],
    "07.1": [
        (
            ["words.txt"],
            "Enter file name:\n\n---------------------------------------------------\n"
            "WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE\nAND REWARDING "
            "ACTIVITY. YOU CAN WRITE PROGRAMS FOR\nA VARIETY OF REASONS, RANGING FROM "
            "MAKING A LIVING\nTO SOLVING A COMPLEX DATA MINING PROBLEM, TO HAVING\nFUN,"
            " TO HELPING SOMEONE ELSE SOLVE A PROBLEM.\n\nTHIS BOOK ASSUMES THAT "
            "EVERYONE NEEDS TO KNOW HOW\nTO PROGRAM AND THAT ONCE YOU KNOW HOW TO "
            "PROGRAM,\nYOU WILL FIGURE OUT WHAT YOU WANT TO DO WITH YOUR\nNEWFOUND "
            "SKILLS.\n---------------------------------------------------\n",
        )
    ],
    "07.2": [(["emails.txt", "X-DSPAM-Confidence"], 0.75072)],
    "08.1": [
        (
            ["romeo.txt"],
            [
                "Arise",
                "But",
                "It",
                "Juliet",
                "Who",
                "already",
                "and",
                "breaks",
                "east",
                "envious",
                "fair",
                "grief",
                "is",
                "kill",
                "light",
                "moon",
                "pale",
                "sick",
                "soft",
                "sun",
                "the",
                "through",
                "what",
                "window",
                "with",
                "yonder",
            ],
        )
    ],
    "08.2": [
        (
            [],
            "---------------------------------\n|  stephen.marquard@uct.ac.za   |\n|   "
            "louis@media.berkeley.edu    |\n|        zqian@umich.edu        |\n|       "
            "rjlowe@iupui.edu        |\n|        zqian@umich.edu        |\n|       rjlo"
            "we@iupui.edu        |\n|        cwen@iupui.edu         |\n|        cwen@iu"
            "pui.edu         |\n|       gsilver@umich.edu       |\n|       gsilver@umic"
            "h.edu       |\n|        zqian@umich.edu        |\n|       gsilver@umich.ed"
            "u       |\n|      wagnermr@iupui.edu       |\n|        zqian@umich.edu    "
            "    |\n|   antranig@caret.cam.ac.uk    |\n| gopal.ramasammycook@gmail.com "
            "|\n|    david.horwitz@uct.ac.za    |\n|    david.horwitz@uct.ac.za    |\n|"
            "    david.horwitz@uct.ac.za    |\n|    david.horwitz@uct.ac.za    |\n|  st"
            "ephen.marquard@uct.ac.za   |\n|   louis@media.berkeley.edu    |\n|   louis"
            "@media.berkeley.edu    |\n|    ray@media.berkeley.edu     |\n|        cwen"
            "@iupui.edu         |\n|        cwen@iupui.edu         |\n|        cwen@iup"
            "ui.edu         |\n---------------------------------\n\nThere are 27 lines "
            "starting with 'From '.\n",
        )
    ],
    "09.1": [([], {"Sat": 1, "Fri": 20, "Thu": 6})],
    "09.2": [([], ("cwen@iupui.edu", 5))],
    "09.3": [
        (
            [],
            {
                "uct.ac.za": 6,
                "media.berkeley.edu": 4,
                "umich.edu": 7,
                "iupui.edu": 8,
                "caret.cam.ac.uk": 1,
                "gmail.com": 1,
            },
        )
    ],
    "10.1": [
        (
            [],
            "--------------\n| hour | frq |\n--------------\n|  04  |  3  |\n|  06  |  "
            "1  |\n|  07  |  1  |\n|  09  |  2  |\n|  10  |  3  |\n|  11  |  6  |\n|  1"
            "4  |  1  |\n|  15  |  2  |\n|  16  |  4  |\n|  17  |  2  |\n|  18  |  1  |"
            "\n|  19  |  1  |\n--------------\n",
        )
    ],
    "10.2": [
        (
            [],
            "a: 7.18%\nb: 1.46%\nc: 2.80%\nd: 5.22%\ne: 13.74%\nf: 2.16%\ng: 2.12%\nh: "
            "3.39%\ni: 7.39%\nj: 0.24%\nk: 0.46%\nl: 4.13%\nm: 2.93%\nn: 7.52%\no: 7.10"
            "%\np: 2.55%\nq: 0.18%\nr: 6.58%\ns: 7.07%\nt: 7.09%\nu: 2.99%\nv: 1.20%\nw"
            ": 1.66%\nx: 0.43%\ny: 2.38%\nz: 0.05%\n",
        )
    ],
    "11.1": [([], 445833)],
    "11.2": [
        (["^Author"], "Enter a regular expression:\nFound 27 lines.\n"),
        (["^X"], "Enter a regular expression:\nFound 216 lines.\n"),
        (["java$"], "Enter a regular expression:\nFound 59 lines.\n"),
        (["2008$"], "Enter a regular expression:\nFound 54 lines.\n"),
    ],
    "12.1": [
        (
            [],
            'Last-Modified: Sat, 13 May 2017 11:22:22 GMT\nETag: "1d3-54f6609240717"\n'
            "Content-Length: 467\nContent-Type: text/plain\n",
        )
    ],
    "12.2": [
        (["http://py4e-data.dr-chuck.net/comments_42.html"], 2553),
        (["http://py4e-data.dr-chuck.net/comments_297236.html"], 2412),
    ],
    "12.3": [
        (["http://py4e-data.dr-chuck.net/known_by_Fikret.html", 2, 4], "Anayah"),
        (["http://py4e-data.dr-chuck.net/known_by_Valeria.html", 17, 7], "Teagen"),
    ],
    "13.1": [
        (["http://py4e-data.dr-chuck.net/comments_42.xml"], 2553),
        (["http://py4e-data.dr-chuck.net/comments_297238.xml"], 2588),
    ],
    "13.2": [
        (["http://py4e-data.dr-chuck.net/comments_42.json"], 2553),
        (["http://py4e-data.dr-chuck.net/comments_297239.json"], 2494),
    ],
    "13.3": [
        (["South Federal University"], "ChIJ1Z9sheJZkFQRDePQqQebCdg"),
        (["Northwestern University"], "ChIJOUw-cAvQD4gRBmHV-me1Nyw"),
    ],
    "15.1": [([], ("41686D65643137",))],
    "15.2": [
        (
            [],
            [
                ("uct.ac.za", 6),
                ("media.berkeley.edu", 4),
                ("umich.edu", 7),
                ("iupui.edu", 8),
                ("caret.cam.ac.uk", 1),
                ("gmail.com", 1),
            ],
        )
    ],
    "15.3": [
        (
            [],
            [
                ("D.T.", "AC/DC", "Who Made Who", "Rock"),
                ("Sink the Pink", "AC/DC", "Who Made Who", "Rock"),
                ("Ride On", "AC/DC", "Who Made Who", "Rock"),
            ],
        )
    ],
    "15.4": [([], ("41616E7961736933303130",))],
}


class TaskSubmitter(TaskSubmitterBase):
    def __init__(self, task_id: str, test_type: Literal["print", "return"]) -> None:
        self._task_data = _ALL_DATA[task_id]
        self._test_type = test_type

    def submit(self, func: Callable) -> None:
        if self._test_type == "print":
            self._test_print(func, self._task_data)
        elif self._test_type == "return":
            self._test_return(func, self._task_data)
        else:
            raise ValueError("Wrong test type. Use 'print' or 'return'.")
