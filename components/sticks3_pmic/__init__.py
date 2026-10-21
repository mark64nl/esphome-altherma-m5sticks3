import esphome.codegen as cg
import esphome.config_validation as cv

from esphome import pins
from esphome.const import CONF_ID

DEPENDENCIES = []
AUTO_LOAD = []

sticks3_pmic_ns = cg.esphome_ns.namespace("sticks3_pmic")
