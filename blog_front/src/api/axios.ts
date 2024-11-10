import axios from "axios";
import cookies from "../lib/cookies.ts";

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,
  headers: {
    Authorization: cookies.getCookie("access_token") ? "Bearer " + cookies.getCookie("access_token") : undefined,
    "Content-Type": "application/json",
  }
});
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response && error.response.data.message === "token unvalid") {
      // Redirect to login page
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);