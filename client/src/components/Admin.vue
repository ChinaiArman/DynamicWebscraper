<template>
    <div>
        <h1>Hello {{ userInfo?.name }}!</h1>
        <h3>You are viewing as an Admin.</h3>
        
        <table>
            <thead>
                <tr>
                    <th>Method</th>
                    <th>Endpoint</th>
                    <th>Requests</th>
                </tr>
            </thead>
            <tbody>
                <!--TODO: add proper data rows-->
                <tr>
                    <td>GET</td>
                    <td>/api/database/get-user-information/</td>
                    <td>1</td>
                </tr>
            </tbody>
        </table>

        <table>
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Email</th>
                    <th>Token (optional column)</th>
                    <th>Total Requests</th>
                </tr>
            </thead>
            <tbody>
                <!--TODO: add proper data rows-->
                <tr>
                    <td>{{ userInfo?.name }}</td>
                    <td>{{ userInfo?.email }}</td>
                    <td>token</td>
                    <td>1</td>
                </tr>
            </tbody>
        </table>
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

<style scoped>
table {
    width: 100%;
    margin-top: 20px;
    border-collapse: collapse;
}

th, td {
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
}

th {
    background-color: #f4f4f4;
    font-weight: bold;
}
</style>