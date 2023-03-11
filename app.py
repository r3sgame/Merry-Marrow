print("Loading... Please wait.")
import tensorflow as tf
import numpy as np

probability_model = tf.keras.models.load_model('model')

print("Welcome to the Merry Marrow CLI! \n")

print("Please enter the donor's age (years): ")
donor_age = input()

print("\n Please enter the recipient age (years): ")
recipient_age = input()

print("\n Please enter the recipient's body mass (kg): ")
recipient_body_mass = input()

print("\n Please enter the CD34 x1e6 per kilogram: ")
CD34_x1e6_per_kg = input()

print("\n Please enter the x1e8 per kilogram: ")
CD3_x1e8_per_kg = input()

print("\n Please enter the CD3 to CD34 ratio: ")
CD3_to_CD34_ratio = input()

print("\n Please enter the ANC recovery: ")
ANC_recovery = input()

print("\n Please enter the PLT recovery: ")
PLT_recovery = input()

print("\n Please enter the time to acute GvHD III/IV: ")
time_to_acute_GvHD_III_IV = input()

print("\n Please enter an estimated survival time (days): ")
survival_time = input()

print("The patient's chance of survival is around: " + str(max(min(abs(probability_model.predict([[float(donor_age), float(recipient_age), float(recipient_body_mass), float(CD34_x1e6_per_kg), float(CD3_x1e8_per_kg), float(CD3_to_CD34_ratio), float(ANC_recovery), float(PLT_recovery), float(time_to_acute_GvHD_III_IV), float(survival_time)]])[0][0]*100),100),0)) + "%")

# print(min(probability_model.predict([[23.34, 4, 36.71, 15.41, 4.979, 5.16, 13, 14, 54, 365]]),100))
# print(min(probability_model.predict([[55.55, 9.5, 36.71, 9.91, 4.979, 5.16, 18, 20, 100000, 365]]),100))