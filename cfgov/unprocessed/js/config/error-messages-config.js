/* ==========================================================================
  Error Messages Config

  These messages are manually mirrored on the Python side in config.py
   ========================================================================== */

'use strict';

var ERROR_MESSAGES = {
  CHECKBOX: {
    REQUIRED: 'Please select at least %s of the options.'
  },
  DATE: {
    INVALID: 'You have entered an invalid date.',
    INVALID_ES: 'La fecha ingresada no es válida.',
    ONE_REQUIRED: 'Please enter at least one date.',
    ONE_REQURED_ES: 'Por favor, ingrese como mínimo una fecha.'
  },
  EMAIL: {
    INVALID: 'You have entered an invalid email address.',
    INVALID_ES: 'La dirección de correo electrónico introducida no es válida.',
    REQUIRED: 'Please enter an email address.',
    REQUIRED_ES: 'Por favor, introduzca una dirección de correo electrónico.'
  },
  PHONE: {
    INVALID: 'You have entered an invalid phone number.',
    INVALID_ES: 'TKTKTK',
    REQUIRED: 'Please enter a phone number.',
    REQUIRED_ES: 'TKTKTK'
  },
  FIELD: {
    INVALID: 'You have entered something invalid for this field.',
    INVALID_ES: 'TKTKTK',
    REQUIRED: 'This field is required.',
    REQUIRED_ES: 'Este campo es obligitario.'
  },
  FORM: {
    SUBMISSION: {
      ERROR: 'There was an error in your submission. Please try again later.',
      ERROR_ES: 'Había un error en su presentación. Por favor, inténtelo más tarde.',
      SUCCESS: 'Your submission was successfully received.',
      SUCCESS_ES: 'Su presentación fue recibido con éxito.'
    }
  },
  DEFAULT: 'Error!',
  DOM: {
    INVALID: 'Invalid dom element was provided.'
  },
  COMMENT: {
    REQUIRED: 'Please enter a comment.',
    REQUIRED_ES: 'Por favor, introduzca un comentario.'
  },
  OPTION: {
    REQUIRED: 'Please select an option.',
    REQUIRED_ES: 'Por favor, seleccione una opción.'
  }
};

module.exports = Object.freeze( ERROR_MESSAGES );
