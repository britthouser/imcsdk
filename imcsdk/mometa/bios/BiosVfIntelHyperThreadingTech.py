"""This module contains the general information for BiosVfIntelHyperThreadingTech ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIntelHyperThreadingTechConsts:
    VP_INTEL_HYPER_THREADING_TECH_DISABLED = "Disabled"
    VP_INTEL_HYPER_THREADING_TECH_ENABLED = "Enabled"
    _VP_INTEL_HYPER_THREADING_TECH_DISABLED = "disabled"
    _VP_INTEL_HYPER_THREADING_TECH_ENABLED = "enabled"
    VP_INTEL_HYPER_THREADING_TECH_PLATFORM_DEFAULT = "platform-default"


class BiosVfIntelHyperThreadingTech(ManagedObject):
    """This is BiosVfIntelHyperThreadingTech class."""

    consts = BiosVfIntelHyperThreadingTechConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIntelHyperThreadingTech", "biosVfIntelHyperThreadingTech", "Intel-HyperThreading-Tech", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfIntelHyperThreadingTech", "biosVfIntelHyperThreadingTech", "Intel-HyperThreading-Tech", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_intel_hyper_threading_tech": MoPropertyMeta("vp_intel_hyper_threading_tech", "vpIntelHyperThreadingTech", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_intel_hyper_threading_tech": MoPropertyMeta("vp_intel_hyper_threading_tech", "vpIntelHyperThreadingTech", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelHyperThreadingTech": "vp_intel_hyper_threading_tech", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIntelHyperThreadingTech": "vp_intel_hyper_threading_tech", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_intel_hyper_threading_tech = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfIntelHyperThreadingTech", parent_mo_or_dn, **kwargs)

