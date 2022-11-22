init -99 python in fae_sprites:

    import store

    FLT_DAY = "day"
    FLT_NIGHT = "night"
    FLT_SUNSET = "sunset"

    # filter dict
    FILTERS = {
        FLT_DAY: store.im.matrix.identity(),
        FLT_NIGHT: store.im.matrix.tint(0.59, 0.49, 0.55),
        FLT_SUNSET: store.im.matrix.tint(0.93, 0.82, 0.78),
    }

    # filter fallback dict
    # key: filter
    # value: filter that should be considered "base" filter
    FLT_FB = {
        FLT_SUNSET: FLT_DAY
    }

    # contains all base filters. These are filtesr without a fallback.
    # this is populated during filter fallback verification and is availabe
    # for use AFTER init level 1.
    # key: filter
    # value: Ignored.
    FLT_BASE = {}

    # should be false until init -1
    __ignore_filters = False

    # global filter variable.
    # NOTE: we keep this out of mas_globals to prevent crashes.
    __flt_global = FLT_DAY


    def add_filter(flt_enum, imx, base=None):
        """
        Adds a filter to the global filters
        You can also use this to override built-in filters.

        NOTE: if you plan to use this, please use it before init level -1
        Filters beyond this level will be ignored.

        NOn-pythonable filter names are ignored

        IN:
            flt_enum - enum key to use as a filter.
            imx - image matrix to use as filter
            base - filter to use as a backup for this filter. Any images
                that are unable to be shown for flt_enum will be revert to
                the base filter.
                This should also be a FLT_ENUM.
                This is checked to make sure it is a valid, preexisting enum,
                so if chaining multiple bases, add them in order.
                If None, no base is given for the flt.
                (Default: None)
        """
        # check init
        if __ignore_filters:
            store.fae_utilities.fae_log.warning(
                "Cannot add filter '{0}' after init -1".format(flt_enum)
            )
            return

        # check name arg able
        if not _test_filter(flt_enum):
            return

        # check base if given
        if base is not None:
            if base not in FILTERS:
                store.fae_utilities.fae_log.warning(
                    "Cannot add filter '{0}' with base '{1}', base flt does not exist".format(flt_enum, base)
                )
                return

            if not _test_filter(base):
                return

            FLT_FB[flt_enum] = base

        FILTERS[flt_enum] = imx



    def get_filter():
        """
        Returns the current filter

        RETURNS: filter to use
        """
        return __flt_global


    def is_filter(flt):
        """
        Checks if the given filter is a valid filter

        IN:
            flt - filter enum to check

        RETURNS: True if valid filter, False if not
        """
        return flt in FILTERS


    def _rslv_flt(flt):
        """
        Gets base filter for a flt.

        IN:
            flt - flt to get base filter for

        RETURNS: base flt for flt, or the flt itself if no base
        """
        return FLT_FB.get(flt, flt)


    def set_filter(flt_enum):
        """
        Sets the current filter if it is valid.
        Invalid filters are ignored.

        IN:
            flt_enum - filter to set
        """
        global __flt_global
        if flt_enum in FILTERS:
            __flt_global = flt_enum


    def _test_filter(flt_enum):
        """
        Checks if this filter enum can be a filter enum.

        Logs to mas log if there are errors

        IN:
            flt_enum - filter enum to test

        RETURNS: True if passed test, False if not
        """
        fake_context = {flt_enum: True}
        try:
            eval(flt_enum, fake_context)
            return True
        except:
            store.fae_utilities.fae_log.warning(
                "Cannot add filter '{0}'. Name is not python syntax friendly".format(flt_enum)
            )

        return False


init -50 python in fae_sprites:

    import store
    import store.fae_outfits as fae_outfits
    import store.fae_utilities as fae_utilities
    import store.fae_gifts as fae_gifts

    ZOOM = "zoom="

    default_zoom_level = 3

    if store.persistent._fae_zoom_setting is None:
        store.persistent._fae_zoom_setting = default_zoom_level
        zoom_level = default_zoom_level
    
    else:
        zoom_level = store.persistent._fae_zoom_setting
    
    zoom_step = 0.05
    default_value_zoom = 1.25
    value_zoom = default_value_zoom
    max_zoom = 20

    default_x = 0
    default_y = 0
    adjust_x = default_x
    adjust_y = default_y
#   y_step = 40
    y_step = 20


    def change_zoom():

        global value_zoom, adjust_y
        if zoom_level > default_zoom_level:
            value_zoom = default_value_zoom + (
                (zoom_level-default_zoom_level) * zoom_step
            )
            adjust_y = default_y + ((zoom_level-default_zoom_level) * y_step)

        elif zoom_level < default_zoom_level:
            value_zoom = default_value_zoom - (
                (default_zoom_level-zoom_level) * zoom_step
            )
            adjust_y = default_y
        else:
            # zoom level is at 10
            value_zoom = default_value_zoom
            adjust_y = default_y

        store.persistent._fae_zoom_setting = zoom_level
    

    def restore_zoom():

        global zoom_level
        zoom_level = default_zoom_level
        change_zoom()
    
    def zoom_out():

        global zoom_level
        zoom_level = 0
        change_zoom()
    
    
    

    FAE_SAYORI_ZORDER = 3

    pose = "sitting"


    _FAE_SAYORI_IMAGES_PATH = "mod_assets/sayori/"

    _FAE_DESK_SPRITE = "desk"

    class Pose():
        sitting = "sitting"

        def __str__(self):
            return self.name

    #EYEBROW DEFS
    class FAEEyebrows():
        a = "normal"
        b = "sad"
        c = "angry"
        d = "sus"
        e = "arched"
        f = "furrowed"
        g = "unamused"
        numb = "numb"

        def __str__(self):
            return self.name

    class FAEBackarms():
        unknown = "a"
        empty = "b"

        def __str__(self):
            return self.name

    #LEFT OR BOTH ARMS ONLY! NO RIGHT ARMS STUFF
    
    class FAEArms():
        cookiebite = "cb"
        cookie = "cookie"
        doublepoint = "double-point"
        folded = "folded"
        lefttouch = "left-fingers-touching"
        leftindex = "left-index-point"
        leftrest = "left-table-rest"
        none = "empty"

        def __str__(self):
            return self.name
    
    
    # RIGHT ARM DEFS
    class FAEArms2():

        folded = "folded"
        rtr = "right-table-rest"
        rf = "right-fist"
        rfpe = "right-finger-pup-ext"
        dp = "double-point"
        hrt = "hand-restingtop"
        none = "empty"
        crossthk = "crossed_thonk"

        def __str__(self):
            return self.name
    
    #EYE DEFS
    class FAEEyes():
        a = "normal-eyes"
        b = "look-left"
        c = "closed-happy"
        d = "wink"
        e = "waaaa"
        f = "dead"
        g = "crazy"
        h = "open-wide"
        i = "squint"
        j = "f1"
        k = "semi-wide"
        l = "closed-sad"
        m = "averted"
        n = "sparkle"
        o = "unamused-eyes"
        p = "midblink"

        
        def __str__(self):
            return self.name
    #HAIR DEFS
    class FAEHair():
        no_bow = "n"
        bow = "b"
       
        def __str__(self):
            return self.name

    #MOUTH DEFS
    class FAEMouth():
        a = "normal-smile"
        b = "weird"
        c = "delicate-agape"
        d = "ajar"
        e = "big-open"
        f = "frown"
        g = "waaaa"
        h = "^"
        i = "blep"
        j = "glub"
        k = "big-smile"
        l = "big_frown"
        m = "drool"
        n = "drool_frown"
        o = "open"
        p = "pout"
        q = "GRIN"
        r = "unamused"
        s = "O_MOUTH"

        def __str__(self):
            return self.name


    class FAETears():
        d_tears = "d_tears"
        happy_d_tears = "happy_d_tears"
        pooled_tears = "pooled_tears"
        sad_d_tears = "sad_d_tears"
        crumbs = "crumbs"
        sweat_drop = "sweat-drop"
        #none = None

        def __str__(self):
            return self.name

    class FAEBlush():
        blushing = "blushing"
        default_cheeks = "default_cheeks"
        red_eyes = "eye-redness"
        gloomy = "gloomy"
        #none = None

        def __str__(self):
            return self.name

    def fae_gen_sprite(
        arms,
        arms2,
        backarm,
        eyes,
        eyebrows,
        mouth,
        blush=None,
        tears=None
    ):
        """
        Creates sprite from given argument
        """

        

        ad_hoc = [
            (1280, 720),
            (0, 0), _FAE_SAYORI_IMAGES_PATH + "table/chair.png",
            (0, 0), "{0}{1}/arms/[Sayori._outfit.clothes.ref_name]/back-arm.png".format(_FAE_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/body/1.png".format(_FAE_SAYORI_IMAGES_PATH, pose),
            #(0, 0), "{0}{1}/clothes/[Sayori._outfit.clothes.ref_name]/1.png".format(_SAYORI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/backarms/[Sayori._outfit.clothes.ref_name]/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, backarm),
            ]

        ad_hoc.extend([
            (0, 0), _FAE_SAYORI_IMAGES_PATH + "table/desk_sh.png",
            (0, 0), _FAE_SAYORI_IMAGES_PATH + "table/desk.png",
            (0, 0), "{0}{1}/arms/[Sayori._outfit.clothes.ref_name]/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, arms),
            (0, 0), "{0}{1}/arms/[Sayori._outfit.clothes.ref_name]/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, arms2),
            #(0, 0), "{0}{1}/hair/{2}.png".format(_SAYORI_IMAGES_PATH, pose, hair),
            (0, 0), "{0}{1}/hair/[Sayori._outfit.hairstyle.ref_name]/a.png".format(_FAE_SAYORI_IMAGES_PATH, pose),
        ])

        if blush:
            ad_hoc.extend([
                (0, 0), "{0}{1}/body/blush/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, blush),
            ])
        
        ad_hoc.extend([
            (0, 0), "{0}{1}/eyes/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, eyes),
            (0, 0), "{0}{1}/mouth/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, mouth),
            ])

        if tears:
            ad_hoc.extend([
                (0, 0), "{0}{1}/eyes/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, tears),
            ])
        
        ad_hoc.extend([
              
            (0, 0), "{0}{1}/eyebrows/{2}.png".format(_FAE_SAYORI_IMAGES_PATH, pose, eyebrows),
            
        ])
        if store.fae_gifts.cookies:

            ad_hoc.extend([
                (0, 0), "mod_assets/images/food/cookies.png",
            ])
        
        if store.fae_gifts.otter:

            ad_hoc.extend([
                (0, 0), "mod_assets/images/acs/otter.png"
            ])
        
        if store.fae_gifts.chibi:

            ad_hoc.extend([
                (0, 0), "mod_assets/images/acs/chibi.png"
            ])
       
        return renpy.display.layout.LiveComposite(
            *ad_hoc
            )

        

init 1 python in fae_sprites:
    import store

    

    POSE_DEF = {
        "sitting": Pose.sitting,
    }
    #EYEBROWS
    EYEBROWS_DEF = {
        "a": FAEEyebrows.a,
        "b": FAEEyebrows.b,
        "c": FAEEyebrows.c,
        "d": FAEEyebrows.d,
        "e": FAEEyebrows.e,
        "f": FAEEyebrows.f,
        "g": FAEEyebrows.g,
        "n": FAEEyebrows.numb
    }

    BACKARM_DEF = {
        "a": FAEBackarms.unknown,
        "b": FAEBackarms.empty
    }

    #Arms with BOTH or ONLY LEFT NO RIGHT
    ARMS_DEF = {
        "a": FAEArms.folded,
        "b": FAEArms.leftindex,
        "c": FAEArms.cookie,
        "d": FAEArms.cookiebite,
        "e": FAEArms.doublepoint,
        #"f": FAEArms.leftindex,
        "f": FAEArms.leftrest,
        "g": FAEArms.lefttouch,
        "h": FAEArms.none
    }
    ARMS2_DEF = {
        "a": FAEArms2.folded,
        "b": FAEArms2.rtr,
        "c": FAEArms2.rf,
        "d": FAEArms2.rfpe,
        "e": FAEArms2.dp,
        "f": FAEArms2.hrt,
        "g": FAEArms2.none,
        "h": FAEArms2.crossthk
    }
    #EYES ONLY
    EYES_DEF = {
        "a": FAEEyes.a,
        "b": FAEEyes.b,
        "c": FAEEyes.c,
        "d": FAEEyes.d,
        "e": FAEEyes.e,
        "f": FAEEyes.f,
        "g": FAEEyes.g,
        "h": FAEEyes.h,
        "i": FAEEyes.i,
        "j": FAEEyes.j,
        "k": FAEEyes.k,
        "l": FAEEyes.l,
        "m": FAEEyes.m,
        "n": FAEEyes.n,
        "o": FAEEyes.o,
        "p": FAEEyes.p
    }
    #HAIR
    HAIR_DEF = {
        "b": FAEHair.bow,
        "n": FAEHair.no_bow
    }
    #MOUTH
    MOUTH_DEF = {
        "a": FAEMouth.a,
        "b": FAEMouth.b,
        "c": FAEMouth.c,
        "d": FAEMouth.d,
        "e": FAEMouth.e,
        "f": FAEMouth.f,
        "g": FAEMouth.g,
        "h": FAEMouth.h,
        "i": FAEMouth.i,
        "j": FAEMouth.j,
        "k": FAEMouth.k,
        "l": FAEMouth.l,
        "m": FAEMouth.m,
        "n": FAEMouth.n,
        "o": FAEMouth.o,
        "p": FAEMouth.p,
        "q": FAEMouth.q,
        "r": FAEMouth.r,
        "s": FAEMouth.s
    }
    
    BLUSH_DEF = {
        "a": FAEBlush.default_cheeks,
        "b": FAEBlush.blushing,
        "c": FAEBlush.gloomy,
        "d": FAEBlush.red_eyes,
        #"": FAEBlush.none
    }

    TEARS_DEF = {
        "e": FAETears.d_tears,
        "f": FAETears.happy_d_tears,
        "g": FAETears.pooled_tears,
        "h": FAETears.sad_d_tears,
        "i": FAETears.crumbs,
        "j": FAETears.sweat_drop,
        #"": FAETears.none
    }

    

    def _exp_renderer(exp_code):
        if len(exp_code) < 6:
            raise ValueError("Invalid expression code: {0}".format(exp_code))
        
        #pose = exp_code[-1]
        #exp_code = exp_code[0]

        eyebrows = exp_code[0]
        exp_code = exp_code[1:]

        backarm = exp_code[0]
        exp_code = exp_code[1:]

        arms = exp_code[0]
        exp_code = exp_code[1:]

        arms2 = exp_code[0]
        exp_code = exp_code[1:]

        #hair = exp_code[0]
        #exp_code = exp_code[1:]

        eyes = exp_code[0]
        exp_code = exp_code[1:]

        mouth = exp_code[0]
        exp_code = exp_code[1:]
        
        blush = None
        tears = None
        


        while exp_code:
            exp_part = exp_code[0]
            exp_code = exp_code[1:]

            if exp_part in BLUSH_DEF:
                blush = exp_part
            #Check if part is a tear
            if exp_part in TEARS_DEF:
                tears = exp_part

            #Otherwise it might be a blush
            

        return {
            #"pose": POSE_DEF[pose],
            "eyebrows": EYEBROWS_DEF[eyebrows],
            "backarm": BACKARM_DEF[backarm],
            "arms": ARMS_DEF[arms],
            "arms2": ARMS2_DEF[arms2],
            #"hair": HAIR_DEF[hair],
            "eyes": EYES_DEF[eyes],
            "mouth": MOUTH_DEF[mouth],
            "blush": BLUSH_DEF.get(blush),
            "tears": TEARS_DEF.get(tears)
            
        }

    


    def _auto_gen(exp_code):
        """
        Generating image from given sprite code
        """

        disp = fae_gen_sprite(**_exp_renderer(exp_code))

        _existing_attr_list = renpy.display.image.image_attributes["sayori"]

        renpy.display.image.images[("sayori", exp_code)] = disp

        #if exp_code not in _existing_attr_list:
        #    _existing_attr_list.append(exp_code)

    def _find_target_override(self):
        
        name = self.name

        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True

        if not isinstance(name, tuple):
            name = tuple(name.split())

        def error(msg):
            self.target = renpy.text.text.Text(
                msg,
                color=(255, 0, 0, 255),
                xanchor=0,
                xpos=0,
                yanchor=0,
                ypos=0
            )

            if renpy.config.debug:
                raise Exception(msg)

        args = [ ]

        while name:
            target = renpy.display.image.images.get(name, None)

            if target is not None:
                break

            args.insert(0, name[-1])
            name = name[:-1]

        if not name:
            if (
                isinstance(self.name, tuple)
                and len(self.name) == 2
                and self.name[0] == "sayori"
            ):
                #Reset name
                name = self.name
                #Generate
                _auto_gen(name[1])
                #Try to get the img again
                target = renpy.display.image.images[name]

            else:
                error("Image '%s' not found." % ' '.join(self.name))
                return False

        try:
            a = self._args.copy(name=name, args=args)
            self.target = target._duplicate(a)

        except Exception as e:
            if renpy.config.debug:
                raise

            error(str(e))

        #Copy the old transform over.
        new_transform = self.target._target()

        if isinstance(new_transform, renpy.display.transform.Transform):
            if self.old_transform is not None:
                new_transform.take_state(self.old_transform)

            self.old_transform = new_transform

        else:
            self.old_transform = None

        return True

    renpy.display.image.ImageReference.find_target = _find_target_override

init -1 python in fae_sprites:

    def show_empty_desk():
        """
        Shows empty desk
        """
        renpy.show(
            "emptydesk",
            tag="emptydesk",
            at_list=[store.i11],
            zorder=store.fae_sprites.FAE_SAYORI_ZORDER - 1
        )

image emptydesk = Composite(
    (1280, 720),
    (0, 0), "mod_assets/sayori/table/chair.png",
    (0, 0), "mod_assets/sayori/table/desk.png"
)



image sayori idle = ConditionSwitch(
    "Affection.isLove(higher=True)", "sayori idle love",
    "Affection.isEnamoured(higher=True)", "sayori idle enamoured",
    "Affection.isAffectionate(higher=True)", "sayori idle affectionate",
    "Affection.isNormal(higher=True)", "sayori idle normal",
    "True", "sayori idle normal",
    predict_all = True
)


image sayori idle love:
    
    block:
        choice:
            "sayori abhfaab"
            pause 5
        
        choice:
            "sayori abhfaaa"
            pause 5
            "sayori abhfpaa"
            pause 0.13
            "sayori abhflaa"
            pause 0.10
            "sayori abhfpaa"
            pause 0.10
        
        repeat

image sayori idle enamoured:

    block:
        choice:
            "sayori abhfaab"
            pause 10
        
        choice:
            "sayori abhfaaa"
            pause 5
            "sayori abhfpaa"
            pause 0.13
            "sayori abhflaa"
            pause 0.10
            "sayori abhfpaa"
            pause 0.10
        
        repeat

image sayori idle affectionate:

    block:
        choice:
            "sayori abhfaaa"
            pause 10
        
        choice:
            "sayori abhfaaa"
            pause 5
            "sayori abhfpaa"
            pause 0.13
            "sayori abhflaa"
            pause 0.10
            "sayori abhfpaa"
            pause 0.10
        
        repeat

image sayori idle normal:

    block:
        choice:
            "sayori abhfaaa"
            pause 10
        
        choice:
            "sayori abhfaaa"
            pause 5
            "sayori abhfpaa"
            pause 0.13
            "sayori abhflaa"
            pause 0.10
            "sayori abhfpaa"
            pause 0.10
        
        repeat


init python:
    def refresh():
        renpy.show("sayori idle normal")

label fae_show_empty_desk(hide_dlg_box=True):
    if hide_dlg_box:
        window hide
    $ store.fae_sprites.show_empty_desk()
    hide sayori with dissolve_sayori
    return

label fae_return_desk(exp="sayori abhfaaa", show_dlg_box=True):

    if show_dlg_box:
        window auto
    $ renpy.show(exp, tag="sayori", at_list=[i11], zorder=store.fae_sprites.FAE_SAYORI_ZORDER)
    $ renpy.with_statement(dissolve_sayori)
    hide emptydesk
    return