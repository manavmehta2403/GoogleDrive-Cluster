def main():

  # spectral clustering

  n = 19090

  k = 2



  # load the graph

  a = import_graph()



  i = a[:, 0]-1

  j = a[:, 1]-1

  v = np.ones((a.shape[0], 1)).flatten()



  A = sparse.coo_matrix((v, (i, j)), shape=(n, n))

  A = (A + np.transpose(A))/2

  old_err_state = np.seterr(divide='raise')

  ignored_states = np.seterr(**old_err_state)

  D = np.diag(1/np.sqrt(np.sum(A, axis=1)).A1)

  D[D == inf] = 0

  L = D @ A @ D



  v, x = np.linalg.eig(L)

  x = x[:, 0:k].real

  x = x/np.repeat(np.sqrt(np.sum(x*x, axis=1).reshape(-1, 1)), k, axis=1)



  # scatter

  plt.scatter(x[:, 0], x[:, 1])

  plt.show()



  # k-means

  kmeans = KMeans(n_clusters=k).fit(x)

  c_idx = kmeans.labels_



  # show cluster

  idx2name = read_team_name()

  for i in range(13):

    print(f'Cluster {i+1}\n***************')

    idx = [index for index, t in enumerate(c_idx) if t == i]

    for index in idx:

      print(idx2name[index])

    print('\n')



  # output file

  output_file(a, idx2name, c_idx)





if __name__ == '__main__':

  main()
