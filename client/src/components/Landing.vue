<template>
    <div>
        <h1>Hello {{ userInfo?.name }}!</h1>

        <h3>Below are your API consumption stats</h3>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            userInfo: null,
        };
    },
    mounted() {
        this.getUserInfo();
    },
    methods: {
        async getUserInfo() {
            try {
                const response = await axios.get('http://localhost:5000/api/database/get-user-information/', {withCredentials: true});   
                console.log(response.data)
                this.userInfo = response.data.user;
            } catch (error) {
                console.error("Error fetching user informatio: ", error);
            }
        }
    }
}
</script>