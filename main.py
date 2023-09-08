import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLines
#This changes matplotlib defaults so it cycles through colors, and makes lines not otherwise specified have a width of 3.0
mpl.rcParams['axes.prop_cycle']= mpl.cycler(color=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'])
mpl.rcParams['lines.linewidth']= 3.0

x = np.linspace(-10, 10, 400) #Set the x-scale.
y = np.linspace(-10, 10, 400) #set the y-scale.
x, y = np.meshgrid(x, y)

#Put some axes on this plot
def axes():
   plt.axhline(0, alpha=.5, color="black", linewidth= 1.0)
   plt.axvline(0, alpha=.5, color="black", linewidth= 1.0)

def leftright_parabola(p, h=0, k=0, lvls=[0]): #used to graph horizontal parabolas
   axes()
   #plots directrix, and label
   plt.axvline(-p, color="gray", linestyle="--", label="Directrix")
   labelLines(plt.gca().get_lines())
   # plots parabola, and labels it using the "fmt" tuple. Notice that the default level for this contour is at 0.
   parabola = plt.contour(x, y, ((y-k)**2 - 4*p*(x-h)), lvls)
   plt.clabel(parabola, parabola.levels, inline=True, fmt={0.0: 'Parabola'}, fontsize=10)
   #Plots Focus and label
   plt.plot(h + p, k, '.', color="black")
   plt.annotate("Focus", (h + p, k), (h + p + 0.1, k + 0.1))

def updown_parabola(p, h=0, k=0, lvls=[0]): #used to graph vertical parabolas
   axes()
   #plots directrix, and label
   plt.axhline(-p, color="gray", linestyle="--", label="Directrix")
   labelLines(plt.gca().get_lines())
   # plots parabola, and labels it using the "fmt" tuple
   parabola = plt.contour(x, y, ((x-h)**2 -4*p*(y-k)), lvls)
   plt.clabel(parabola, parabola.levels, inline=True, fmt={0.0: 'Parabola'}, fontsize=10)
   #Plots Focus and label
   plt.plot(h, k+p, '.', color="black")
   plt.annotate("Focus", (h, k+p), (h + 0.1, k + p + 0.1))

def horizontal_ellipse(a, b, h=0, k=0, lvls=[0]): #used to graph horizontal ellipses
  axes()
  if a<b: #checks to see that the a value is larger than the b, as that is required in an ellipse
    print("a has to be larger than b")
    return
  # plots ellipse, and labels it using the "fmt" tuple
  ellipse = plt.contour(x, y, (((x-h)**2)/(a**2) + ((y-k)**2)/(b**2) - 1), lvls)
  plt.clabel(ellipse, ellipse.levels, inline=True, fmt={0.0: 'Ellipse'}, fontsize=10)
  c = (a**2 - b**2) ** 0.5
  #Plots Focus and label
  plt.plot(h + c, k, '.', color="black")
  plt.plot(h - c, k, '.', color="black")
  plt.annotate("Focus", (h + c, k), (h + c - 1, k + 0.2))
  plt.annotate("Focus", (h - c, k), (h - c - 0.1, k + 0.2))

def vertical_ellipse(a, b, h=0, k=0, lvls=[0]): #used to graph vertical ellipses
  axes()
  if a<b: #checks to see that the a value is larger than the b, as that is required in an ellipse
    print("a has to be larger than b")
    return
  # plots ellipse, and labels it using the "fmt" tuple
  ellipse = plt.contour(x, y, (((x-h)**2)/(b**2) + ((y-k)**2)/(a**2) - 1), lvls)
  plt.clabel(ellipse, ellipse.levels, inline=True, fmt={0.0: 'Ellipse'}, fontsize=10)
  c = (a**2 - b**2) ** 0.5
  #Plots Foci and labels
  plt.plot(h, k + c, '.', color="black")
  plt.plot(h, k - c, '.', color="black")
  plt.annotate("Focus", (h, k + c), (h + 0.2, k + c - 1))
  plt.annotate("Focus", (h, k - c), (h + 0.2, k - c - 0.1))

def leftright_hyperbola(a, b, h=0, k=0, lvls=[0]): #used to graph horizontal hyperbolas
  axes()
  #plots asymptotes using the asymptote formula for horizontal hyperbolas
  plt.axline((4, b/a*(4-h) + k), slope=b/a, color="gray", linestyle="--")
  plt.axline((-3, -b/a*(-3-h) + k), slope = -b/a, color="gray", linestyle="--")
  # plots ellipse, and labels it using the "fmt" tuple
  hyperbola = plt.contour(x, y, (((x-h)**2)/(a**2) - ((y-k)**2)/(b**2) - 1), lvls)
  plt.clabel(hyperbola, hyperbola.levels, inline=True, fmt={0.0: 'Hyperbola'}, fontsize=10)
  c = (a**2 + b**2) ** 0.5
  #Plots Foci and labels
  plt.plot(h + c, k, '.', color="black")
  plt.plot(h - c, k, '.', color="black")
  plt.annotate("Focus", (h + c, k), (h + c - 1, k + 0.2))
  plt.annotate("Focus", (h - c, k), (h - c - 0.1, k + 0.2))

def updown_hyperbola(a, b, h=0, k=0, lvls=[0]): #used to graph vertical hyperbolas
  axes()
  #plots asymptotes using the asymptote formula for vertical hyperbolas
  plt.axline((0, a/b*(-h) + k), slope=a/b, color="gray", linestyle="--")
  plt.axline((0, -a/b*(-h) + k), slope = -a/b, color="gray", linestyle="--")
  # plots ellipse, and labels it using the "fmt" tuple
  hyperbola = plt.contour(x, y, (((y-k)**2)/(a**2) - ((x-h)**2)/(b**2) - 1), lvls)
  plt.clabel(hyperbola, hyperbola.levels, inline=True, fmt={0.0: 'Hyperbola'}, fontsize=10)
  c = (a**2 + b**2) ** 0.5
  #Plots Foci and labels
  plt.plot(h, k + c, '.', color="black")
  plt.plot(h, k - c, '.', color="black")
  plt.annotate("Focus", (h, k + c), (h + 0.2, k + c - 1))
  plt.annotate("Focus", (h, k - c), (h + 0.2, k - c - 0.1))

def plot_conic(e, p, operation, trig): #code to graph a conic in polar form given e, p, the operation in the denominator (+ or -) and the trig function
  fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}) #sets the graph to polar mode
  theta = np.arange(0, (2 * np.pi), 0.01) #creates an np array of radian values from 0 to 2 pi, incrementing by 0.01
  for rad in theta:
    r = 0
    if operation == '+':
      if trig == 'cos':
        r = ((e * p) / (1 + (e * np.cos(rad)))) #if the operation given is + and the function is cosine, this form of the equation is used
      else:
        r = ((e * p) / (1 + (e * np.sin(rad)))) #if the operation given is + and the function is sine, this form of the equation is used
    else:
      if trig == 'cos':
        r = ((e * p) / (1 - (e * np.cos(rad)))) #if the operation given is - and the function is cosine, this form of the equation is used
      else:
        r = ((e * p) / (1 - (e * np.sin(rad)))) #if the operation given is - and the function is sine, this form of the equation is used
    ax.plot(rad+(r<0)*np.pi, np.abs(r), 'g.') #used to ensure it doesn't treat negative radial values literally, plotting them as negative numbers as it rotates negative values by pi radians. 
    ax.set_rlim(bottom=0, top=5) #also used to avoid it treating negative values literally

def polar_to_rectangular(equation): #equation is entered in the form (a/(b-cf(theta)), where a, b, and c are numbers, f is either cosine or sine, and theta is in radians and can be expressed as the symbol or any other word
  #These values are found using substrings of the equation
  denom_operation = '+' if '+' in equation.split("/")[1][2:] else '-' #to determine if the denominator is using addition or subtraction
  trigFunc = equation.split("/")[1].split(denom_operation)[1][1:4] #to determine if there is cosine or sine used in the denominator
  const = int(equation.split("/")[1].split(denom_operation)[0][1:2])  #finds the number to the left of the coefficient value
  numer = int(equation.split("/")[0]) #finds the numerator
  coef = int(equation.split("/")[1].split(denom_operation)[1][0:1]) #finds the number being multiplied to the trig function
  """These values are based on the coefficients of the general form of a conic function: Ax^2 + By^2 + Cxy + Dx + Ey + F = 0, and no C is used here because no rotation is being used
  Work on how to derive these values from the general equation is shown on this google drive link: https://drive.google.com/file/d/1Mx9mkx1fp0sHDKtW6ePYpgQjReKJKlqe/view?usp=sharing"""
  A = (const**2-coef**2) if trigFunc == "cos" else const**2
  B = (const**2-coef**2) if trigFunc == "sin" else const**2
  D = 0
  if trigFunc=="cos":
      D = -2*numer*coef if denom_operation == "-" else 2*numer*coef
  E = 0
  if trigFunc=="sin":
      E = -2*numer*coef if denom_operation == "-" else 2*numer*coef
  F = -(numer**2)
  
  h = -D/(2*A) if A!=0 else F/E
  k = -E/(2*B) if B!=0 else F/E
  right_side_sum = -F + A*(h**2) + B*(k**2)
  a = abs((right_side_sum/A))**0.5 if A!=0 else 0
  b = abs((right_side_sum/B))**0.5 if B!=0 else 0
  eccentricity = coef/const
  
  if eccentricity < 1: #for ellipse
    if trigFunc == "sin":
      vertical_ellipse(b, a, h, k)
    else:
      horizontal_ellipse(a, b, h, k)
  elif eccentricity == 1: #for parabola
    p = 0
    if trigFunc == "sin": #for vertical hyperbola
      p = -E/4
      updown_parabola(p, h, k)
    else: #for horizontal hyperbola
      p = -D/4
      leftright_parabola(p, h, k)
  else: #for hyperbola
    if trigFunc == "sin": #for vertical hyperbola
      updown_hyperbola(a, b, h, k)
    else: #for horizontal hyperbola
      leftright_hyperbola(a, b, h, k)
  plot_conic(eccentricity, numer/coef, denom_operation, trigFunc) #plots the eqution in polar form using the plot_conic function
polar_to_rectangular("3/(2+1costheta)") 
plt.show()