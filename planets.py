import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Netunono",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Urano",
            (980,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Saturno",
            (760,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Jupiter",
            (570,370),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (200,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Terra",
            (290,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Marte",
            (390,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (120,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (0,0,255)
            )


cv2.imshow('resultado',img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg',img)
