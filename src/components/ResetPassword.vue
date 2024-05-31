<script>
import axios from 'axios';

export default{
    components: {
        axios
    },
    data() {
        return {
            show_password: false,
            old_password: '',
            confirm_password: '',
            user_info: {
                email: "",
                password: "",
            },
            rules: {
                // todo
                correctPasswords: v => true || 'Не правильный пароль',
                passwordMatch: v => /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(v) || 'Пароль должен содержать хотя бы одну цифру, одну маленькую и одну большую букву, и быть длиннее 8 символов',
                passwordsEquals: v => v === this.user_info.password || 'Пароли не совпадают',
            }
            }
    },
    methods: {
        reset_password(){
            // axios.post(`#`, [this.user_info]) // add the link
        },
    }

}
</script>

<template>
    <v-container fluid class="container">
        <v-form class="registration-form">
            <img src="" alt="" class="registration-logo"> 
            <h1 class="registration-title">
                Смена пароля
            </h1>
            <hr class="registration-divider">
            <v-text-field 
                :append-inner-icon="show_password ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show_password ? 'text' : 'password'"
                counter
                @click:append-inner="show_password = !show_password"
                prepend-inner-icon="mdi-lock-outline"
                class="registration-row-input" 
                label="Старый пароль" 
                required 
                v-model="this.old_password"
                :rules="[rules.correctPasswords]"
            ></v-text-field>
            <v-text-field 
                :type="show_password ? 'text' : 'password'"
                counter
                @click:append-inner="show_password = !show_password"
                prepend-inner-icon="mdi-lock-outline"
                class="registration-row-input" 
                label="Новый пароль" 
                required 
                v-model="this.user_info.password"
                :rules="[rules.passwordMatch]"
            ></v-text-field>
            <v-text-field 
                :type="show_password ? 'text' : 'password'"
                counter
                @click:append-inner="show_password = !show_password"
                prepend-inner-icon="mdi-lock-outline"
                class="registration-row-input" 
                label="Подтверждение пароля" 
                required 
                v-model="this.confirm_password"
                :rules="[rules.passwordsEquals]"
            ></v-text-field>
            <v-btn type="submit" class="registration-submit" @click="reset_password()" block>Подтверждить</v-btn>
        </v-form>
    </v-container>
</template>

<style scoped>

.container{
    justify-content: center;
    align-items: center;
    width: 100%;
}

.registration-title{
    margin: 10px;
    font-size: 30px;
}

a{
    color: #ff96a6;
    text-decoration: none;
}

a:hover{
    color: 1px solid #fd6e8c;
    translate: 300ms;
}

.registration-divider{
    margin-top: 20px;
    justify-content: center;
    height: 4px;
    width: 100px;
    background-color: #ff96a6;
    border: none;
}

.registration-form{
    margin-top: 50px;
    padding: 30px;
    border-radius: 50px;
    background-color: #fdf0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 576px;
}

.registration-row-input{
    width: 500px;
    margin-top: 30px;
}

.register-signin{
    text-align: center;
    display: block;
}

.registration-submit{
    margin-top: 50px;
    margin-bottom: 30px;
    cursor: pointer;
    padding: 10px;
    border-radius: 30px;
    color: white;
    background-color: #ff96a6;
    border: none;
    height: 60px;
    width: 100%;
}

.registration-submit:hover{
    background-color: #fd6e8c;
    transition: 300ms;
} 
</style>