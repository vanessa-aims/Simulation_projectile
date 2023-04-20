#Author Bralyne Vanessa Kamga Matoukam
#we are trying to simulate the projectile position and velocity at t>0
import numpy as np
import pandas as pd#I would like to return my results as a data frame
def projectile_motion(initial_velocity, angle, time_step, total_time):#define 
     #the function projectile_motion with four entries: the initial velocity,
     #the angle, the time step and the total time
    g=9.8 #gravitional acceleration constant
    t=np.arange(0,total_time,time_step)#the range of time starting from 0 and
    #ending to total_time with respect to the time_step
    alpha=angle*(np.pi/180)#convert the angle in radians as the entry value 
    #should be in degree and numpy uses only radians angles to compute cosine, 
    #sine, tan an so on
    Y=[] #initialisation of a list of y position of the projectile
    X=[]#initialisation of a list of x position of the projectile
    V_X=[]#initialisation of a list of vx : the x coordinate of the
    #projectile's velocity
    V_Y=[]#initialisation of a list of vy : the y coordinate of the 
    #projectile's velocity
    for i in t:# for each value of the time
        y=-0.5*g*i**2+initial_velocity*i*np.sin(alpha)#this is the formula of 
        #the y coordinate of a projectile'motion under the influence of gravity.
        x=initial_velocity*i*np.cos(alpha)#this is the formula of the x 
        #coordinate of a projectile'motion under the influence of gravity.
        v_x=initial_velocity*np.cos(alpha)#this is the formula of the x
        #coordinate of the velocity of a projectile'motion under the influence 
        #of gravity.
        v_y=-g*i+initial_velocity*np.sin(alpha)#this is the formula of the y 
        #coordinate of the velocity of a projectile'motion under the influence 
        #of gravity.
        Y.append(y)#store all y values in the list Y
        X.append(x)#store all x values in the list X
        V_X.append(v_x)#store all v_x values in the list V_X
        V_Y.append(v_y)#store all v_y values in the list V_Y
    # Store all the lists into a dictionary
    dataset = {'Time': t, 'X-velocity': V_X,'Y-velocity': V_Y,'X-position':X,
               'Y-position': Y}
    # Convert the dictionary into the Pandas Dataframe
    df = pd.DataFrame(dataset)#Pandas data frame
    pd.set_option('display.max_rows',None)#display max rows
    #df.to_excel('data.xlsx')#save the data frame as excel doc
    return df #return the data frame
#we can try with these values projectile_motion(10,45,0.01,2) 
