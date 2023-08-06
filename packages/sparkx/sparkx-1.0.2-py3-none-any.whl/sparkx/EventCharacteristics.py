import numpy as np
from sparkx.Particle import Particle
from sparkx.Lattice3D import Lattice3D

class EventCharacteristics:
    """
    This class computes event-by-event characteristics, e.g., eccentricities
    or certain densities.

    Parameters
    ----------
    event_data: list, numpy.ndarray or Lattice3D
        List or array containing particle objects for one event, or a lattice containing the relevant densities.

    Attributes
    ----------
    event_data_: list, numpy.ndarray or Lattice3D
        List or array containing particle objects for one event, or a lattice containing the relevant densities.
    has_lattice_: bool
        Contains information if characteristics are derived from a lattice or particles

    Methods
    -------
    set_event_data:
        Overwrites the event data.
    eccentricity:
        Computes the spatial eccentricity.
    eccentricity_from_particles:
        Computes the spatial eccentricity from particles.
    eccentricity_from_lattice:
        Computes the spatial eccentricity from a 3D lattice.

    Examples
    --------

    .. highlight:: python
    .. code-block:: python
        :linenos:

        >>> from sparkx.Oscar import Oscar
        >>> from sparkx.EventCharacteristics import EventCharacteristics
        >>>
        >>> OSCAR_FILE_PATH = [Oscar_directory]/particle_lists.oscar
        >>>
        >>> # Oscar object containing all events
        >>> oscar = Oscar(OSCAR_FILE_PATH)
        >>>
        >>> event_characterization = EventCharacteristics(oscar)
        >>> event_characterization.eccentricity(2, weight_quantitiy = "number")

    """
    def __init__(self, event_data):
        self.set_event_data(event_data)

    def set_event_data(self, event_data):
        """
        Overwrites the event data.

        Parameters
        ----------
        event_data : list, numpy.ndarray, or Lattice3D
            List or array containing particle objects for one event, or a
            lattice containing the relevant densities.

        Raises
        ------
        TypeError
            If the input is not a list or numpy.ndarray when deriving
            characteristics from particles.
            If at least one element in the input is not of type Particle.
        """
        # check if the input is a Lattice3D object
        if isinstance(event_data, Lattice3D):
            self.event_data_ = event_data
            self.has_lattice_ = True
        else:
            # check that the input is a list/numpy.ndarray containing Particle objects
            if not isinstance(event_data, (list, np.ndarray)):
                raise TypeError('The input is not a list nor a numpy.ndarray.')
            for particle in event_data:
                if not isinstance(particle, Particle):
                    raise TypeError('At least one element in the input is not a ' +
                                    'Particle type.')
            self.event_data_ = event_data
            self.has_lattice_ = False

    def eccentricity_from_particles(self,harmonic_n, weight_quantity = "energy"):
        """
        Computes the spatial eccentricity from particles.

        Parameters
        ----------
        harmonic_n : int
            The harmonic order for the eccentricity calculation.
        weight_quantity : str, optional
            The quantity used for particle weighting.
            Valid options are "energy", "number", "charge", or "baryon number".
            Default is "energy".

        Returns
        -------
        complex
            The complex-valued eccentricity.

        Raises
        ------
        ValueError
            If the harmonic order is less than 1.
            If the weight quantity is unknown.
        """
        real_eps=0
        imag_eps=0
        norm=0
        if harmonic_n < 1:
            raise ValueError("Eccentricity is only defined for positive expansion orders.")
        for particle in self.event_data_:
            if weight_quantity == "energy":
                weight = particle.E
            elif weight_quantity == "number":
                weight = 1
            elif weight_quantity == "charge":
                weight = particle.charge
            elif weight_quantity == "baryon number":
                weight = particle.baryon_number
            else:
                raise ValueError("Unknown weight for eccentricity")
            x = particle.x
            y = particle.y
            #Exception for dipole asymmetry
            if harmonic_n == 1:
                rn = (x**2+y**2)**(3/2.0)
            else:
                rn = (x**2+y**2)**(harmonic_n/2.0)
            t = np.arctan2(y,x)
            real_eps += rn*np.cos(harmonic_n*t)*weight
            imag_eps += rn*np.sin(harmonic_n*t)*weight
            norm += rn*weight
        return real_eps/norm + (imag_eps/norm)*1j

    def eccentricity_from_lattice(self,harmonic_n):
        """
        Computes the spatial eccentricity from a 3D lattice. Takes all z-values
        into account.

        Parameters
        ----------
        harmonic_n : int
            The harmonic order for the eccentricity calculation.

        Returns
        -------
        complex
            The complex-valued eccentricity.

        Raises
        ------
        ValueError
            If the harmonic order is less than 1.
        """
        real_eps=0
        imag_eps=0
        norm=0
        if harmonic_n < 1:
            raise ValueError("Eccentricity is only defined for positive expansion orders.")
        for i, j, k in np.ndindex(self.event_data_.grid_.shape):
            x, y, z = self.event_data_.get_coordinates(i, j, k)
            #Exception for dipole asymmetry
            if harmonic_n == 1:
                rn = (x**2+y**2)**(3/2.0)
            else:
                rn = (x**2+y**2)**(harmonic_n/2.0)
            t = np.arctan2(y,x)
            lattice_density = self.event_data_.get_value_by_index(i, j, k)
            real_eps += rn*np.cos(harmonic_n*t)*lattice_density
            imag_eps += rn*np.sin(harmonic_n*t)*lattice_density
            norm += rn*lattice_density
        return real_eps/norm + (imag_eps/norm)*1j

    def eccentricity(self,harmonic_n,weight_quantity = "energy"):
        """
        Computes the spatial eccentricity.

        Parameters
        ----------
        harmonic_n : int
            The harmonic order for the eccentricity calculation.
        weight_quantity : str, optional
            The quantity used for particle weighting.
            Valid options are "energy", "number", "charge", or "baryon number".
            Default is "energy".

        Returns
        -------
        complex
            The complex-valued eccentricity.

        Raises
        ------
        ValueError
            If the harmonic order is less than 1.
        """
        if self.has_lattice_:
            return self.eccentricity_from_lattice(harmonic_n)
        else:
            return self.eccentricity_from_particles(harmonic_n, weight_quantity)
