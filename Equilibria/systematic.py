import numpy as np
import scipy.optimize as spo

class acid(object):
    '''An object used to define an acidic species.

    This object takes the Ka and/or pKa values for an acidic species, its
    charge in the fully protonated, and its concentration in solution. Using
    this information, it can then calculate several properties of this species
    in solution.

    Parameters
    ----------
    Ka = None : This is a single Ka value or an iterable of several Ka values.
    Either this value or pKa needs to be defined. The other can then be
    calculated, which is the preferred method.

    pKa = None : This is a single pKa value or an iterable of several pKa
    values. See Ka for more details.

    charge = None : This is the charge of the fully protonated form of this
    acid.

    conc = None : The formal concentration of this acid in solution.

    '''
    def __init__(self, Ka=None, pKa=None, charge=None, conc=None):
        # Do a couple quick checks to make sure that everything has been
        # defined.
        if Ka == None and pKa == None:
            raise ValueError(
                "You must define either Ka or pKa values.")
        elif charge == None:
            raise ValueError(
                "The maximum charge for this acid must be defined.")

        # Make sure both Ka and pKa are calculated. For lists of values, be
        # sure to sort them to ensure that the most acidic species is defined
        # first.
        elif Ka == None:
            if isinstance(pKa, (int, float)):
                self.pKa = np.array( [pKa,], dtype=float)
            else:
                self.pKa = np.array(pKa, dtype=float)
                self.pKa.sort()
            self.Ka = 10**(-self.pKa) 
        elif pKa == None:
            if isinstance(Ka, (int, float)):
                self.Ka = np.array( [Ka,], dtype=float)
            else:
                self.Ka = np.array(Ka, dtype=float)
                self.Ka.sort()
            self.pKa = -np.log10(self.Ka)
        # This temporary Ka array will be used to calculate alpha values. It
        # starts with an underscore so that it won't be confusing for others.
        self._Ka_temp = np.append(1., self.Ka)
        
        # Make a list of charges for each species defined by the Ka values.
        self.charge = np.arange(charge, charge - len(self.Ka) - 1, -1)
        # Make sure the concentrations are accessible to the object instance.
        self.conc = conc 

    def alpha(self, pH):
        '''Return the fraction of each species at a given pH.

        This returns a Numpy list of fractional speciation at a given
        solution. The returned list will be ordered as per the Ka/pKa values,
        with the most acidic component listed first.

        '''
        # If the given pH is not a list/array, be sure to convert it to one
        # for future calcs.
        if isinstance(pH, (int, float)):
            pH = [pH,]
        pH = np.array(pH, dtype=float)

        # Calculate the concentration of H3O+. If multiple pH values are
        # given, then it is best to construct a two dimensional array of
        # concentrations.
        h3o = 10.**(-pH)
        if len(h3o) > 1:
            h3o = np.repeat( h3o.reshape(-1, 1), len(self._Ka_temp), axis=1)

        # These are the powers that the H3O+ concentrations will be raised.
        power = np.arange(len(self._Ka_temp))
        # Calculate the H3O+ concentrations raised to the powers calculated
        # above (in reverse order).
        h3o_pow = h3o**( power[::-1] )
        # Calculate a cumulative product of the Ka values. The first value
        # must be 1.0, which is why _Ka_temp is used instead of Ka.
        Ka_prod = np.cumproduct(self._Ka_temp)
        # Multiply the H3O**power values times the cumulative Ka product.
        h3o_Ka = h3o_pow*Ka_prod

        # Return the alpha values. The return signature will differ is the
        # shape of the H3O array was 2-dimensional. 
        if len(h3o.shape) > 1:
            den = h3o_Ka.sum(axis=1)
            return h3o_Ka/den.reshape(-1,1)
        else:
            den = h3o_Ka.sum()
            return h3o_Ka/den

class spectator(object):
    """A nonreactive ion class.

    This object defines things like K+ and Cl-, which contribute to the
    overall charge balance, but do not have any inherent reactivity with
    water.
    
    Parameters
    ----------
    charge : The formal charge of the ion.
    conc : The concentration of this species in solution.

    """
    def __init__(self, charge=None, conc=None):
        if charge == None:
            raise ValueError(
                "The charge for this ion must be defined.")

        self.charge = charge 
        self.conc = conc

    def alpha(self, pH):
        '''Return the fraction of each species at a given pH.

        Because this is a non-reactive ion class, this will always return a
        Numpy array containing just 1.0 for all pH values.

        '''
        return np.array([1.0,])

class salt(object):
    def __init__(self, *species):
        self.species = species


    def _diff_pos_neg(self, pH):
        # Calculate the h3o and oh concentrations and sum them up.
        h3o = 10.**(-pH)
        oh = (10.**(-14))/h3o
        x = (h3o - oh)
    
        # Go through all the species that were given, and sum up their
        # charge*concentration values into our total sum.
        for s in self.species:
            x += (s.conc*s.charge*s.alpha(pH)).sum()
         
        # Return the absolute value so it never goes below zero.
        return np.abs(x)

    def pHsolve(self, guess=7.0):
        self.pHsolution = spo.minimize(self._diff_pos_neg, guess, 
                method='Nelder-Mead')
        self.pH = self.pHsolution.x



if __name__ == '__main__':
    #a = acid(pKa=1.987, charge=-1, conc=0.01)
    #k = neutral(1, 0.02)
    #s = salt(a, k)

    #a = acid(Ka = 1.75e-5, charge=0, conc=0.01) 
    #s = salt(a) 

    # Ammonium phosphate
    a = acid(pKa=[2.148, 7.198, 12.375], charge=0, conc=1.e-3)
    b = acid(pKa=9.498, charge=1, conc=3.e-3)
    #k = neutral(charge=1, conc=1.e-4)
    #k = neutral(charge=-1, conc=3.e-3)
    s = salt(a, b)

    # HCl, just need to define the amount of Cl-. The solver will find the
    # correct H+
    #b = neutral(charge=-1, conc=1e-8)
    #s = salt(b)

    # KOH, just need to define the amount of K+, solver takes care of the
    # rest.
    #a = neutral(charge=+1, conc=0.1)
    #s = salt(a)

    s.pHsolve()
    print s.pH

    # Ammonium phosphate
#    j = []
#    hcl = np.linspace(1.e-8, 1.e-2, 100)
#    a = acid(pKa=[2.148, 7.198, 12.375], charge=0, conc=1.e-3)
#    b = acid(pKa=9.498, charge=1, conc=3.e-3)
#    for i in hcl:
#        k = neutral(charge=1, conc=i)
#        #k = neutral(charge=-1, conc=i)
#        s = salt(a, b, k)
#        s.pHsolve()
#        j.append(s.pH[0])
#

