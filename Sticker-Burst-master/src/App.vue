<template>
    <v-app>
        <v-toolbar extended>
            <img align-center id="logo" src="../sticker_bar.png"/>
            <v-spacer/>
            <!--LOGIN BEGINS HERE-->
            <div>
                <v-layout id="login" row wrap>
                    <v-flex xs4>
                    <v-text-field v-if="loggedIn == 0"
                            v-model="input.username"
                            label="Username"
                            hint="At least 8 characters"
                            clearable
                            @click:append="show1 = !show1"
                    ></v-text-field>
                    </v-flex>
                    <v-spacer/>
                    <v-flex xs4>
                        <v-text-field v-if="loggedIn == 0"
                                v-model="input.password"
                                :rules="[rules.required, rules.min]"
                                :type="show1 ? 'text' : 'password'"
                                position="relative"
                                name="input-10-1"
                                label="Password"
                                hint="At least 8 characters"
                                clearable
                                @click:append="show1 = !show1"
                        ></v-text-field>
                    </v-flex>
                    
                    <v-flex xs3>
                        <v-btn v-if="loggedIn == 0"
                                color="success"
                                v-on:click="login">Login
                        </v-btn>
                    </v-flex>
                    <v-flex xs3>
                        <v-btn v-if="loggedIn"
                                color="error"
                                v-on:click="logout">Logout
                        </v-btn>
                    </v-flex>

                </v-layout>
                </v-layout>
            </div>
             <!--LOGIN ENDS HERE-->
        </v-toolbar>
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap>
                <v-flex xs12>
                        <img id="topbar" src="../anim.gif" />
                </v-flex>
                <v-flex xs6>
                    <v-card>
                        <!--IMAGE UPLOAD BEGINS HERE-->
                    <div id="app">
                    <div v-for="item in items">

                        <div v-if="!item.image">
                        <v-layout column wrap align-center>
                        <v-flex x12 sm3>
                            <h2>Upload Your Photo Here!</h2>
                        </v-flex>
                        <v-flex x12 sm3>
                            <img src="../upload_sign.png" />
                        </v-flex>
                        <v-flex x12 sm3>
                            <div class="file-upload">
                            <div class="file-select">
                                <div class="file-select-button" id="fileName">Choose File</div>
                                <div class="file-select-name" id="noFile">No file chosen...</div> 
                                <input type="file" name="chooseFile" id="chooseFile" accept="image/*" @change="onFileChange(item, $event), emitGlobalClickEvent()">
                            </div>
                            </div>
                        </v-flex>
                        </v-layout>
                        </div>

                        <div v-else>
                        <v-layout column>
                            <v-flex x12 sm3>
                            <img id="displayedPic" :src="item.image" />
                            </v-flex>
                            <v-flex x12 sm3>
                            <v-btn color="primary" @click="removeImage(item),emitGlobalClickEvent()">Choose Another Image</v-btn>
                            </v-flex>
                        </v-layout>
                        </div>

                    </div>
                    </div> 
                    <!--IMAGE UPLOAD ENDS HERE-->                       
                    </v-card>
                </v-flex xs6>
                <v-flex xs6>
                    <v-card>
                        <!--STICKER THEME SELECTION BEGINS HERE-->
<div v-if="imageChosen">
 <!-- Tier 0 (no login) Buttons -->
  <div v-if="!buttonSelected">
      <h2>Sticker Theme Selection!</h2>
      <div v-if="tierlevel0">
          <v-btn depressed small color="error" @click="EventFunction()">
            I like to live on the wild side. Randomize me!
          </v-btn>
      </div>

      <v-container fluid class="pa-0">
        <!-- Tier 1 (basic login) and part of Tier 2 (premium login) buttons -->
        <div v-if="tierlevel1 || tierlevel2">
          <v-layout row wrap>
            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(0)">
                <img src="../sticker/avatar/001-man.png" />
              </v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(1)">
                <img src="../sticker/cooking/012-chef.png" />
              </v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(2)">
                <img src="../sticker/payment/041-bitcoin.png" />
              </v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(3)">
                <img src="../sticker/recycle/047-recycling-2.png" />
              </v-btn>
            </v-flex>
          </v-layout>
        </div>

        <!-- Tier 2 (premium) only Buttons -->
        <div v-if="tierlevel2">
          <v-layout row wrap>
            <v-flex xs12 sm3>
              <v-btn flat disabled large></v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(4)">
                <img src="../sticker/social_networking/facebook.png" />
              </v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat large @click="ClickFunction(5)">
                <img src="../sticker/Avatar/001-man.png" />
              </v-btn>
            </v-flex>

            <v-flex xs12 sm3>
              <v-btn flat disabled large></v-btn>
            </v-flex>
          </v-layout>
        </div>

      </v-container>
    </div>

    <div v-else>
      <!--when you click a button, a confirm screen shows-->
      <p> Are you sure you want to use this theme?</p>
      <v-layout row wrap justify-center>
        <div>
          <v-btn depressed small left color="primary" @click="EventFunction()">
            Yes
          </v-btn>
        </div>
        <div>
          <v-btn depressed small left color="error" @click="BackToMain()">
            No
          </v-btn>
        </div>
      </v-layout>
    </div>

</div>
<div v-else>
Please upload an image first
</div>
<!--sticker theme selection ends here-->                        
                    </v-card>
                </v-flex xs6>
            </v-layout>
        </v-container>
    </v-app>
</template>

<script>
export default {

name: 'App',

data () {
      return {
        show1: false,
        input: {
          username: "",
          password: ""
        },
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        },
        accounts: [
          "garrett4",
          "texasfight",
          "csrules4",
          "chicken4"
        ],
        passwords: [
          "odomodom",
          "longhorns",
          "aerorules",
          "biscuit4"
        ],
        access: [
          1,
          1,
          2,
          2
        ],
        loop: 0,
        loggedIn: 0,
        tierlevel: 0,
            items: [
       {
         image: false,
       },
    ],
    imageChosen: false,
    //Decides what tier
    tierlevel0: true,
    tierlevel1: false,
    tierlevel2: false,
    //button function items
    buttonSelected: false,
    stickerNumber: 0,
    themes: ["Avatar", "Cooking", "Payment", "Recycling", "Social Networking", "BB"],
    theme: '',
    displaySelection: false,
      }
},
methods: {
          login: function (event) {
        this.loggedIn = 0
        for (this.loop = 0; this.loop < this.accounts.length; this.loop++) {
          if(this.input.username == this.accounts[this.loop] && this.input.password == this.passwords[this.loop] && this.loggedIn == 0) {
            alert('Logged in as ' + this.input.username + '\nTier ' + this.access[this.loop] + ' Access')
            this.loggedIn = 1
            this.tierlevel = this.access[this.loop]
            
            if(this.tierlevel==0){
                this.tierlevel0=true;
                this.tierlevel1=false;
                this.tierlevel2=false;
            }
            else if(this.tierlevel==1){
                this.tierlevel0=false;
                this.tierlevel1=true;
                this.tierlevel2=false;
            }
            else {
                this.tierlevel0=false;
                this.tierlevel1=false;
                this.tierlevel2=true;                
            }
            }
          }
        
        if (this.loggedIn == 0) {
          alert('Invalid Login Credentials. Please Try Again.')
          this.tierlevel = 0

        }
      },
      logout: function (event) {
        this.loggedIn = 0
        alert('Logged Out')
        this.tierlevel0 = true
        this.tierlevel1 = false
        this.tierlevel2 = false
      },
      onFileChange(item, e) {
      this.imageChosen = true;
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(item, files[0]);
    },

    createImage(item, file) {
      var image = new Image();
      var reader = new FileReader();

      reader.onload = (e) => {
        item.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function (item) {
      this.imageChosen = false;
      item.image = false;
    },

    ClickFunction: function (stickerNumber){
      this.buttonSelected = true
      this.theme = this.themes[stickerNumber]
    },
    BackToMain: function () {
      this.buttonSelected = false

    },
    WhichTheme: function () {
      return this.theme;
    },
}
};

</script>

<style>
#logo {
    height: 110px;
    position: relative;
    top: 33px;
}
#topbar {
    height: 150px;
}
#login {
  position: relative;
  top: 32px;
}
#app {
  text-align: center;
}
#displayedPic {
    height: 300px;
}
button {

}
.file-upload{display:block;text-align:center;font-family: Helvetica, Arial, sans-serif;font-size: 12px;}
.file-upload .file-select{display:block;border: 2px solid #dce4ec;color: #34495e;cursor:pointer;height:40px;line-height:40px;text-align:left;background:#FFFFFF;overflow:hidden;position:relative;}
.file-upload .file-select .file-select-button{background:#dce4ec;padding:0 10px;display:inline-block;height:40px;line-height:40px;}
.file-upload .file-select .file-select-name{line-height:40px;display:inline-block;padding:0 10px;}
.file-upload .file-select:hover{border-color:#34495e;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload .file-select:hover .file-select-button{background:#34495e;color:#FFFFFF;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload.active .file-select{border-color:#3fa46a;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload.active .file-select .file-select-button{background:#3fa46a;color:#FFFFFF;transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;}
.file-upload .file-select input[type=file]{z-index:100;cursor:pointer;position:absolute;height:100%;width:100%;top:0;left:0;opacity:0;filter:alpha(opacity=0);}
.file-upload .file-select.file-select-disabled{opacity:0.65;}
.file-upload .file-select.file-select-disabled:hover{cursor:default;display:block;border: 2px solid #dce4ec;color: #34495e;cursor:pointer;height:40px;line-height:40px;margin-top:5px;text-align:left;background:#FFFFFF;overflow:hidden;position:relative;}
.file-upload .file-select.file-select-disabled:hover .file-select-button{background:#dce4ec;color:#666666;padding:0 10px;display:inline-block;height:40px;line-height:40px;}
.file-upload .file-select.file-select-disabled:hover .file-select-name{line-height:40px;display:inline-block;padding:0 10px;}

#displayedPic {
  height: 300px;
}
  img {
    height: 35px;
  }
</style>
