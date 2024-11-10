import Auth from "../domain/auth";
import { apiClient } from "./axios";

export const login = async (auth: Auth) => {
  let res = await apiClient.post<Auth>("/users/login/", auth);
  return res.data;
};