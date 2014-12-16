from wtforms import Form, fields, validators


class ReportForm(Form):
    """
    This class defines the online form as well as the validators
    The entries are variables necessary in our modeling
    """
    Auction = fields.SelectField('Auction Provider for the Purchase',
                                 [validators.InputRequired()],
                                 choices=[('ADESA', 'ADESA'),
                                          ('MANHEIM', 'MANHEIM'),
                                          ('OTHER', 'OTHER')])
    VehicleAge = fields.IntegerField('Vehicle Age in Year',
                                     [validators.InputRequired(),
                                      validators.NumberRange(min=0, max=20)])
    Make = fields.SelectField('Vehicle Manufacturer',
                              [validators.InputRequired()],
                              choices=[('CHEVROLET', 'CHEVROLET'),
                                       ('DODGE', 'DODGE'), ('FORD', 'FORD'),
                                       ('CHRYSLER', 'CHRYSLER'),
                                       ('PONTIAC', 'PONTIAC'), ('KIA', 'KIA'),
                                       ('NISSAN', 'NISSAN'),
                                       ('HYUNDAI', 'HYUNDAI'),
                                       ('SATURN', 'SATURN'),
                                       ('JEEP', 'JEEP'), ('TOYOTA', 'TOYOTA'),
                                       ('MITSUBISHI', 'MITSUBISHI'),
                                       ('MAZDA', 'MAZDA'),
                                       ('MERCURY', 'MERCURY'),
                                       ('BUICK', 'BUICK'), ('GMC', 'GMC'),
                                       ('HONDA', 'HONDA'),
                                       ('SUZUKI', 'SUZUKI'),
                                       ('OLDSMOBILE', 'OLDSMOBILE'),
                                       ('ISUZU', 'ISUZU'),
                                       ('VOLKSWAGEN', 'VOLKSWAGEN'), 
                                       ('SCION', 'SCION'), ('VOLVO', 'VOLVO'),
                                       ('LINCOLN', 'LINCOLN'), 
                                       ('SUBARU', 'SUBARU'),
                                       ('ACURA', 'ACURA'), ('MINI', 'MINI'),
                                       ('CADILLAC', 'CADILLAC'),
                                       ('INFINITI', 'INFINITI'),
                                       ('PLYMOUTH', 'PLYMOUTH'),
                                       ('LEXUS', 'LEXUS')])
    Trim = fields.SelectField('Vehicle Trim Level',
                              [validators.InputRequired()],
                              choices=[('1', '1'), ('150', '150'), ('2', '2'),
                                       ('3', '3'), ('Adv', 'Adv'),
                                       ('Bas', 'Bas'), ('CE', 'CE'),
                                       ('CX', 'CX'), ('Cla', 'Cla'),
                                       ('Cus', 'Cus'), ('ES', 'ES'),
                                       ('EX', 'EX'), ('Edd', 'Edd'),
                                       ('Edg', 'Edg'), ('GL', 'GL'),
                                       ('GLS', 'GLS'), ('GS', 'GS'),
                                       ('GT', 'GT'), ('L20', 'L20'),
                                       ('L30', 'L30'), ('LE', 'LE'),
                                       ('LS', 'LS'), ('LT', 'LT'),
                                       ('LX', 'LX'), ('LXi', 'LXi'),
                                       ('Lar', 'Lar'), ('Lim', 'Lim'),
                                       ('Nor', 'Nor'), ('OTHER', 'OTHER'),
                                       ('S', 'S'), ('SE', 'SE'),
                                       ('SEL', 'SEL'), ('SES', 'SES'),
                                       ('SLE', 'SLE'), ('SLT', 'SLT'),
                                       ('ST', 'ST'), ('STX', 'STX'),
                                       ('SXT', 'SXT'), ('Spo', 'Spo'),
                                       ('Tou', 'Tou'), ('W/T', 'W/T'),
                                       ('XE', 'XE'), ('XL', 'XL'),
                                       ('XLS', 'XLS'), ('XLT', 'XLT'),
                                       ('ZX3', 'ZX3'), ('ZX4', 'ZX4'),
                                       ('i', 'i'), ('s', 's')])
    SubModel = fields.SelectField('Vehicle Submodel',
                                  [validators.InputRequired()],
                                  choices=[('2D CONVERTIBLE',
                                            '2D CONVERTIBLE'),
                                           ('2D COUPE', '2D COUPE'),
                                           ('2D QUAD', '2D QUAD'),
                                           ('4D CUV', '4D CUV'),
                                           ('4D HATCHBACK', '4D HATCHBACK'),
                                           ('4D MINIVAN', '4D MINIVAN'),
                                           ('4D PASSENGER', '4D PASSENGER'),
                                           ('4D SEDAN', '4D SEDAN'),
                                           ('4D SPORT', '4D SPORT'),
                                           ('4D SUV', '4D SUV'),
                                           ('4D SUV-PICKUP', '4D SUV-PICKUP'),
                                           ('4D UTILITY', '4D UTILITY'),
                                           ('4D WAGON', '4D WAGON'),
                                           ('CREW CAB', 'CREW CAB'),
                                           ('EXT CAB', 'EXT CAB'),
                                           ('MINIVAN 2.4L', 'MINIVAN 2.4L'),
                                           ('MINIVAN 3.3L', 'MINIVAN 3.3L'),
                                           ('MINIVAN 3.8L', 'MINIVAN 3.8L'),
                                           ('OTHER', 'OTHER'),
                                           ('PASSENGER 3.4L',
                                            'PASSENGER 3.4L'),
                                           ('PASSENGER 3.8L',
                                            'PASSENGER 3.8L'),
                                           ('PASSENGER 3.9L',
                                            'PASSENGER 3.9L'),
                                           ('PASSENGER EXT', 'PASSENGER EXT'),
                                           ('QUAD CAB', 'QUAD CAB'),
                                           ('REG CAB', 'REG CAB'),
                                           ('SPORT UTILITY', 'SPORT UTILITY'),
                                           ('WAGON 2.7L', 'WAGON 2.7L'),
                                           ('WAGON 3.5L', 'WAGON 3.5L')])
    Color = fields.SelectField('Vehicle Color', [validators.InputRequired()],
                               choices=[('BEIGE', 'BEIGE'), ('BLACK', 'BLACK'),
                                        ('BLUE', 'BLUE'), ('BROWN', 'BROWN'),
                                        ('GOLD', 'GOLD'), ('GREEN', 'GREEN'),
                                        ('GREY', 'GREY'), ('MAROON', 'MAROON'),
                                        ('NOT AVAIL', 'NOT AVAIL'),
                                        ('ORANGE', 'ORANGE'),
                                        ('OTHER', 'OTHER'), 
                                        ('PURPLE', 'PURPLE'),
                                        ('RED', 'RED'), ('SILVER', 'SILVER'),
                                        ('WHITE', 'WHITE'),
                                        ('YELLOW', 'YELLOW')])
    Transmission = fields.SelectField('Vehicle Transmission Type',
                                      [validators.InputRequired()],
                                      choices=[('AUTO', 'AUTO'),
                                               ('MANUAL', 'MANUAL')])
    WheelType = fields.SelectField('Vehicle Wheel Type',
                                   [validators.InputRequired()],
                                   choices=[('Alloy', 'Alloy'),
                                            ('Covers', 'Covers'),
                                            ('Special', 'Special')])
    VehOdo = fields.IntegerField('Vehicle Odometer Reading',
                                 [validators.InputRequired(),
                                  validators.NumberRange(min=0, max=300000)])
    Nationality = fields.SelectField("Manufacturer's Country",
                                     [validators.InputRequired()],
                                     choices=[('AMERICAN', 'AMERICAN'),
                                              ('OTHER', 'OTHER'), 
                                              ('OTHER ASIAN', 'OTHER ASIAN'),
                                              ('TOP LINE ASIAN',
                                               'TOP LINE ASIAN')])
    Size = fields.SelectField("Size Category of the Vehicle",
                              [validators.InputRequired()],
                              choices=[('COMPACT', 'COMPACT'),
                                       ('CROSSOVER', 'CROSSOVER'),
                                       ('LARGE', 'LARGE'),
                                       ('LARGE SUV', 'LARGE SUV'),
                                       ('LARGE TRUCK', 'LARGE TRUCK'),
                                       ('MEDIUM', 'MEDIUM'),
                                       ('MEDIUM SUV', 'MEDIUM SUV'),
                                       ('SMALL SUV', 'SMALL SUV'),
                                       ('SMALL TRUCK', 'SMALL TRUCK'),
                                       ('SPECIALTY', 'SPECIALTY'),
                                       ('SPORTS', 'SPORTS'), ('VAN', 'VAN')])
    temp = 'Acquisition price for this vehicle in average condition at' + \
           ' time of purchase'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRAcquisitionAuctionAveragePrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in' + \
           'the above Average condition at time of purchase'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRAcquisitionAuctionCleanPrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in the retail' + \
           'market in average condition at time of purchase'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRAcquisitionRetailAveragePrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in the retail market' + \
           'in above average condition at time of purchase'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRAcquisitonRetailCleanPrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in average' + \
           'condition as of current day'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRCurrentAuctionAveragePrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in the above' + \
           'condition as of current day'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRCurrentAuctionCleanPrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in the retail' + \
           'market in average condition as of current day'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRCurrentRetailAveragePrice = fields.FloatField(temp, temp_val)
    temp = 'Acquisition price for this vehicle in the retail' + \
           'market in above average condition as of current day'
    temp_val = [validators.InputRequired(),
                validators.NumberRange(min=0, max=100000)]
    MMRCurrentRetailCleanPrice = fields.FloatField(temp, temp_val)
    VNST = fields.SelectField("State of the Purchase",
                              [validators.InputRequired()],
                              choices=[('AL', 'AL'), ('AZ', 'AZ'),
                                       ('CA', 'CA'), ('CO', 'CO'),
                                       ('FL', 'FL'), ('GA', 'GA'),
                                       ('IA', 'IA'), ('ID', 'ID'),
                                       ('IL', 'IL'), ('IN', 'IN'),
                                       ('KY', 'KY'), ('LA', 'LA'),
                                       ('MD', 'MD'), ('MO', 'MO'),
                                       ('MS', 'MS'), ('NC', 'NC'),
                                       ('NJ', 'NJ'), ('NM', 'NM'),
                                       ('NV', 'NV'), ('OH', 'OH'),
                                       ('OK', 'OK'), ('OR', 'OR'),
                                       ('OTHER', 'OTHER'), ('PA', 'PA'),
                                       ('SC', 'SC'), ('TN', 'TN'),
                                       ('TX', 'TX'), ('UT', 'UT'),
                                       ('VA', 'VA'), ('WA', 'WA'),
                                       ('WV', 'WV')])
    VehBCost = fields.FloatField('Acquisition cost paid for the vehicle at ' +
                                 'time of purchase',
                                 [validators.InputRequired(),
                                  validators.NumberRange(min=0, max=100000)])
    IsOnlineSale = fields.SelectField('If purchased online',
                                      [validators.InputRequired()],
                                      choices=[('1', 'YES'), ('2', 'NO')])
    WarrantyCost = fields.FloatField('Warranty price (term=36month ' +
                                     'and millage=36K)',
                                     [validators.InputRequired(),
                                      validators.NumberRange(min=0,
                                                             max=20000)])
