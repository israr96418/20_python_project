import qrcode

def QR_code_generator(text):
    #pass parameter to QRCode function
    qr_code = qrcode.QRCode(
        version=1,            # version parameter--> integer 1 to 40 it controll the size of qrcode, smallest version is 1(21*21 matrx)
        #error_correction--> control error correction used for qrcode , four constant are made avaliable
        #1:ERROR_CORRECT_L--> About 7% or less error can be corrected
        #2:ERROR_CORRECT_M(default)--> About 15% or less error can be corrected
        #3:ERROR_CORRECT_Q--> About 25% or less error can be corrected
        #4:ERROR_CORRECT_H--> About 30% or less error can be corrected
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    #add data to qr_code object/instance
    qr_code.add_data(text)
    #create qrcode
    qr_code.make(fit=True)
    #qrcode image create
    image = qr_code.make_image(fill_color='black', back_color='white')
    image.save('github.png')



if __name__ == '__main__':
    your_qrcode = input("Enter your data to embed into qrcode: ")
    QR_code_generator(your_qrcode)