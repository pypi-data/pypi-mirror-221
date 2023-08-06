# ![Image](./GhostEye.png "GhostEye") physical_sources

This is a collection of classes meant to provide access to acoustic source levels that were contained within the initial
release of the Counter Listener Acoustic Warfare Software (CLAWS). But with the changes to the releasibility of the code
and data from CLAWS, a number of classes were removed from the distribution. 

```mermaid
classDiagram
    
    class INoiseSource{
        <<interface>>>>
        predict(location)
    }
    
    class IPointSource~INoiseSource~{
        <<interface>>
        Length reference_distance
        predict(location)
    }
    
    class IAnalyticSource{
        <<interface>>
        # Array coefficients
        predict(location)
    }
    
    class IdealDipoleX{
        Length dipole_separation
        float calculation_time
        predict(location)
    }
    
    class ISphereSource{
        <<interface>>
        +Length reference_distance
        +predict(location)
    }
    
    class HarmonicSeries~ISphereSource~{
        #Array coefficients
        +Length reference_distance
        +float MSE
        +float Rsq
        +predict(location)
    }    
    
    class HarmonicSpectrum~ISphereSource~{
        #Array<HarmonicSeries> metrics
    }
    
    class InterpolatedHarmonicSpectrum~IsphereSource~{
        #Array sources
        +float power_setting
        predict(location)
    }
    
    class GridMetric~ISphereSource~{
        +reference_distance
        +predict(location)
    }
    
    class GridSpectrum~ISphereSource~{
        +predict(location)
    }
    
    class AircraftType{
        <<enumeration>>
        +Military
        +Civilian
    }
    class DataCollectionType{
        <<enumeration>>
        +Measured
        +Estimated
    }
    
    class InterpolationCode{
        <<enumeration>>
        +Fixed
        +Parallel
        +Variable
    }
    
    class NoiseFilePowerSetting{
        +value
        +units
        +upper_limit
        +lower_limit
    }
    
    class NoiseFileAcousticSource~IPointSource~{
        +source_type
        +freuqency_resolution
        +minimum_frequency_band
        +maximum_freqency_band
        +vehicle_type
        +interpolation_code
        +data_collection_type
        +number_of_microphones_in_average
        +directivity_angle
        +perceived_noise_level
        +tone_corrected_pnl
        +a_weighted_level
        +tone_corrected_a_weighted_level
        +sound_exposure_level
        +tone_corrected_sel
        +effective_perceived_noise_level
        +tone_correction
        +aircraft_id
        +operational_power_code
        +operational_type_code
        +engine_name
        +engine_count
        +drage_configuration
        +source
        +collection_date
        +reference_speed
        +reference_temperature
        +reference_humidity
        +power_setting_description
        +power_settings
        +write_date(filename)
        #load_data(contents, index)
        +predict(location)
    }
    
    class NoiseFileStaticAcousticSource~NoiseFileAcousticSource~{
        +measurement_count
        +reference_pressure
        #_load_data(contents, index)
        +write_data(writer)
        +predict(location)
    }
    
    INoiseSource<|--IPointSource : Inheritance
    INoiseSource<|--IAnalyticSource : Inheritance
    INoiseSource<|--ILineSource : Inheritance
    INoiseSource<|--ISphereSource : Inheritance
    IAnalyticSource<|--IdealDipoleX : Inheritance
    ISphereSource<|--HarmonicSeries : Inheritance
    HarmonicSpectrum-->HarmonicSeries : Contains
    ISphereSource<|--HarmonicSpectrum : Inheritance
    ISphereSource<|--InterpolatedHarmonicSpectrum : Inheritance
    InterpolatedHarmonicSpectrum-->HarmonicSpectrum : Contains
    IPointSource <|--NoiseFileAcousticSource : Inheritance
    NoiseFileAcousticSource-->AircraftType : Contains
    NoiseFileAcousticSource-->DataCollectionType : Contains
    NoiseFileAcousticSource-->InterpolationCode : Contains
    NoiseFileAcousticSource-->NoiseFilePowerSetting : Contains
    NoiseFileAcousticSource<|--NoiseFileStaticAcousticSource : Inheritance
    ISphereSource<|--GridMetric : Inheritance
    GridSpectrum-->GridMetric : Contains
    ISphereSource<|--GridSpectrum : Inheritance
```