from flask import g
from flask import Flask  , url_for , render_template , request , redirect 
from flask.views import View
from flask import g 
import os , random , string 
from werkzeug.utils  import secure_filename
import time
import sqlite3
from sqlite3 import Error
import uuid 
import datetime
import TimeCop as Generate_Timestamp
import Users_Class_Trigger as UserJunction

app=Flask(__name__)




 
# app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
# defining function
  return render_template("404.html")


# CLASS BASED VIEW DECLARATIONS 
# Clothes & General Accessories 



# Function To Return Sequence Strings For Token Synchronixation 


def Generate_Sequence():
    return uuid.uuid4()  





class AuthSecurity(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = UserJunction.create_connection("./ static/Databases/ShadowMemmory.db")
        Context_Keys = ('Username' , 'Password')
        Context_Value = "Unknown"
        if request.method == 'POST':
                # - Action Zone
                UserDict = {}
                UserDict = request.form
                for k in UserDict.values():
                    print(k)
                # Database Profiling
                UserID = request.form.get("UserString")
                g.UserID = UserID 
                CryptoIdentifier = request.form.get("CryptoString")
                Security_Captcha = UserJunction.Query_User_Existence(Connection_Manager, UserID)
                Crypto_Captcha = UserJunction.Query_CryptoHash_Existence(Connection_Manager, CryptoIdentifier)
                print(Security_Captcha)
                if (Security_Captcha != None ):
                    if(Crypto_Captcha != None):
                        return redirect(url_for("Catalogues" , UserID  = UserID ))
                    else:
                        return redirect("/Auth")
                else:
                    users = " jsdjsd "
                    return render_template('AuthController.html' )
        else:
                return render_template('AuthController.html' )




class ImportCriteria(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        Connection_Manager = UserJunction.create_connection("./static/Databases/ShadowMemmory.db")
        if request.method == 'POST':
            AccountData = request.form
            for Chunk in AccountData.values(): 
                print(Chunk)
            UserString = str(request.form.get("UsrString")) 
            Profile_Location = UserString + ".jpg"
            Credential = list(AccountData.values())
            Credential.append(Profile_Location)
            UserJunction.Create_UserProfile(Connection_Manager , Credential)
            return redirect(url_for('Auth'))
        else:
            User = "Uni-Identified"
            return render_template('ImportAccount.html', User=User , Generate_Sequence = Generate_Sequence )


class GarmentFactory(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)


# Jewelery
class PebbleRocks(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)



# Electronics 
class Mechatronics(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)




class Furniture(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)



class PowerHouse(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)


class InternalDecorations(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)



class Cutlery(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('DoctorLayout.html', User=User)


class HomeStack(View):
    def dispatch_request(self):
        GalleryObject=os.listdir(os.path.join(app.static_folder, "Conceptuals/"))
        ObjectTrack = len(GalleryObject)
        UserID = ""
        return render_template('DoctorLayout.html', ObjectTrack=ObjectTrack , GalleryObject=GalleryObject , UserID = UserID )



class ShoppingCart(View):
    def dispatch_request(self):
        CartElement = "0"
        return render_template('ShoppingCart.html', CartElement=CartElement)


class BillingPoint(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('BillingProfile.html', User=User)




class AccountReference(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('BillingInvoice.html', User=User)



class AccountProfile(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('AccountEdition.html', User=User)



class Contacts(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('Contact.html', User=User)



class GeneralOrders(View):
    def dispatch_request(self):
        User = "Uni-Identified"
        return render_template('GeneralOrders.html', User=User)


class Descriptor(View):
    def dispatch_request(self):
        Object=os.listdir(os.path.join(app.static_folder, "Conceptuals/"))
        Symbiotism = Object[:5]
        User = "Uni-Identified"
        return render_template('Descriptor.html', User=User , Symbiotism=Symbiotism )


app.add_url_rule('/STORE/', view_func=Furniture.as_view('STORE'))
app.add_url_rule('/Electronics/', view_func=Mechatronics.as_view('Electronics'))
app.add_url_rule('/GarmentsFactory/', view_func=GarmentFactory.as_view('GarmentsFactory'))
app.add_url_rule('/Jewelery/', view_func=PebbleRocks.as_view('Jewelery'))
app.add_url_rule('/Energy/', view_func=PowerHouse.as_view('Energy'))
app.add_url_rule('/HouseDecor/', view_func=InternalDecorations.as_view('HouseDecor'))
app.add_url_rule('/CutleryItems/', view_func=Cutlery.as_view('CutleryItems'))
app.add_url_rule('/Fashion/', view_func=HomeStack.as_view('Fashion'))
app.add_url_rule('/Cart/', view_func=ShoppingCart.as_view('Cart'))
app.add_url_rule('/Billing/',view_func=BillingPoint.as_view('Billing'))
app.add_url_rule('/Accounts/',view_func=AccountProfile.as_view('Accounts'))
app.add_url_rule('/Auth/',view_func=AuthSecurity.as_view('Auth'))
app.add_url_rule('/CreateAccount/',view_func=ImportCriteria.as_view('CreateAccount'))
app.add_url_rule('/PaymentInfo/',view_func=AccountReference.as_view('PaymentInfo'))
app.add_url_rule('/Contact/',view_func=Contacts.as_view('Contact'))
app.add_url_rule('/Tag/',view_func=Descriptor.as_view('Tag'))
app.add_url_rule('/Dispatch/',view_func=GeneralOrders.as_view('Dispatch'))


if __name__=='__main__':
   app.run(host="0.0.0.0" , debug="False" )

