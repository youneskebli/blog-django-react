import Writer from "../domain/writer";
import { apiClient } from "./axios";

export const getWriters = async () => {
  let res = await apiClient.get<Writer[]>("/");
  return res.data;
};

export const getWriterById = async (id: number) => {
  let res = await apiClient.get<Writer>(`/${id}`);
  return res.data;
};

export const createWriter = async (Writer: Omit<Writer, "id">) => {
  let res = await apiClient.post<Writer>("/", Writer);
  return res.data;
};

export const patchWriter = async (Writer: Partial<Omit<Writer, "id">>) => {
  let res = await apiClient.patch<Writer>("/", Writer);
  return res.data;
};
