<script>
import AuthorizationForm from './components/AuthorizationForm.vue';
import CandidateTable from './components/CandidateTable.vue';
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';
import RegisterForm from './components/RegisterForm.vue';

export default{
    components: {
        Header,
        Footer,
        RegisterForm,
        AuthorizationForm,
        CandidateTable
    },
    name: 'App',
    data() {
        return {
            logo_name: "IP-position"
        }
    },
    computed: {

    },
    methods: {
        
    }
}
</script>

<template>
    <v-app>
        <!-- <CandidateTablie/> -->
        <AuthorizationForm :logo_name="this.logo_name"/>
    </v-app>
</template>